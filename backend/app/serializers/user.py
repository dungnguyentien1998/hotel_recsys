from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from app.models import User, Role
from app.exceptions import Unauthenticated, ValidationError, InvalidToken
# from app.utils.mailer import send_new_account_email, send_forgot_password
# from app.utils.security import TokenType, decode_token


class LoginSerializer(serializers.Serializer):
    # Login data
    email = serializers.CharField()
    password = serializers.CharField()

    # Check login credentials
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise Unauthenticated


class RegisterSerializer(serializers.ModelSerializer):
    # Register data
    password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = [*User.editable_fields(), 'password_confirm']

    def create(self, validated_data):
        # Get password and confirm password
        password = validated_data['password']
        password_confirm = validated_data['password_confirm']
        # Check if role admin
        if validated_data['role'] == Role.ADMIN:
            raise ValidationError('Can\'t create user with role admin')
        # Check if password equals confirm password
        if password != password_confirm:
            raise ValidationError(_('Password and password confirm mismatch'))
        # Remove confirm password
        [validated_data.pop(key) for key in ('password', 'password_confirm')]
        # Activate user
        validated_data['is_active'] = True
        # Create user
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        # send_new_account_email(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    # User data to represent, used for admin
    class Meta:
        model = User
        exclude = ['deleted', 'last_login', 'password']


class ActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_active']

    def update(self, instance, validated_data):
        # Activate or deactivate user
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance


class AccountSerializer(serializers.ModelSerializer):
    # User data to represent, used for user
    class Meta:
        model = User
        fields = [field for field in User.editable_fields() if field not in ['email', 'password', 'role']]

    def update(self, instance, validated_data):
        # Update user profile
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance


# class ActivateAccountSerializer(serializers.Serializer):
#     # User data to activate by email
#     token = serializers.CharField()
#     email = serializers.EmailField()
#
#     def validate(self, validated_data):
#         payload = decode_token(token=validated_data['token'],
#                                callback=send_new_account_email,
#                                params={'user': User.objects.get(email=validated_data['email'])})
#         if not payload or payload['type'] != TokenType.NEW_ACCOUNT:
#             raise InvalidToken
#         return User.objects.get(uuid=payload['sub'])
#
#     def update(self, instance, validated_data=None):
#         instance.is_active = True
#         instance.save()


# class UserUuidField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.uuid
#
#     class Meta:
#         model = User


# class ForgotPasswordSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#
#     # Validate email forgot password
#     def validate(self, validated_data):
#         User.objects.get(email=validated_data['email'])
#         return validated_data
#
#     # Send link to email forgot password
#     def create(self, validated_data):
#         user = User.objects.get(email=validated_data['email'])
#         send_forgot_password(user=user)
#         return user


# class ResetPasswordSerializer(serializers.Serializer):
#     # Data to reset password
#     token = serializers.CharField()
#     password = serializers.CharField()
#     password_confirm = serializers.CharField()
#
#     def validate(self, validated_data):
#         # Get password and confirm password
#         password = validated_data['password']
#         password_confirm = validated_data['password_confirm']
#         # Check if password equals confirm password
#         if password != password_confirm:
#             raise ValidationError(_('Password and password confirm mismatch'))
#         # Get token and validate token type
#         payload = decode_token(token=validated_data['token'])
#         if not payload or payload['type'] != TokenType.FORGOT_PASSWORD:
#             raise InvalidToken
#         user = User.objects.get(uuid=payload['sub'])
#         return user, password
#
#     def update(self, instance, validated_data):
#         # Update password
#         instance.set_password(validated_data)
#         instance.save()


# class ChangePasswordSerializer(serializers.Serializer):
#     # Data to change password
#     old_password = serializers.CharField()
#     password = serializers.CharField()
#     password_confirm = serializers.CharField()
#
#     def validate(self, data):
#         user = self.context['request'].user
#         # Get password and confirm password
#         password = data['password']
#         password_confirm = data['password_confirm']
#         # Check if password equals confirm password
#         if password != password_confirm:
#             raise ValidationError(_('Password and password confirm mismatch'))
#         if not user.check_password(password):
#             raise Unauthenticated
#         return user, password
#
#     def update(self, instance, validated_data=None):
#         # Update password
#         instance.set_password(validated_data)
#         instance.save()
