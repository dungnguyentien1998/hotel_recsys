from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from app import models
from app.utils.security import TokenType, generate_token
from app.utils.serializer_validator import validate_serializer
from app.serializers import LoginSerializer, RegisterSerializer, AccountSerializer, UserSerializer, ActiveSerializer, \
    ActivateAccountSerializer, ForgotPasswordSerializer, ResetPasswordSerializer, ChangePasswordSerializer
from app.exceptions import Unauthorized
from app.tasks import demo_task, process_tasks, calculate_sim
import datetime
from django.db import connection


class Login(APIView):
    permission_classes = (AllowAny,)

    # Login api
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        validate_serializer(serializer=serializer)
        user = serializer.validated_data
        token = generate_token(obj=user.uuid, _type=TokenType.AUTHENTICATION)
        cursor = connection.cursor()
        cursor.execute("Select * from background_task")
        row = cursor.fetchall()
        if not row:
            # demo_task(schedule=0, repeat=3600)
            calculate_sim(schedule=0, repeat=3600)
        process_tasks()
        return Response({
            'success': True,
            'token': token
        })


class Register(APIView):
    permission_classes = (AllowAny,)

    # Create user
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        validate_serializer(serializer=serializer)
        user = serializer.save()
        return Response({
            'success': True,
            'user': UserSerializer(user).data
        })


class User(APIView):
    # List users
    def get(self, request):
        user = request.user
        if user.role != models.Role.ADMIN:
            raise Unauthorized
        users = models.User.objects.all()
        return Response({
            'success': True,
            'users': UserSerializer(users, many=True).data
        })


class UserDetail(APIView):
    # Get one user
    def get(self, request, user_id):
        user = models.User.objects.get(uuid=user_id)
        return Response({
            'success': True,
            'user': UserSerializer(user).data
        })

    # Active or deactive user
    def put(self, request, user_id):
        user = models.User.objects.get(uuid=user_id)
        serializer = ActiveSerializer(data=request.data)
        validate_serializer(serializer=serializer)
        serializer.update(instance=user, validated_data=serializer.validated_data)
        return Response({
            'success': True,
            'user': UserSerializer(user).data
        })


class Account(APIView):
    # Get profile
    def get(self, request):
        user = request.user
        return Response({
            'success': True,
            'user': UserSerializer(user).data
        })

    # Update profile
    def put(self, request):
        serializer = AccountSerializer(data=request.data)
        validate_serializer(serializer=serializer)
        user = serializer.update(instance=request.user, validated_data=serializer.validated_data)
        return Response({
            'success': True,
            'user': UserSerializer(user).data
        })


class ActivateAccount(APIView):
    permission_classes = (AllowAny,)

    # Activate account for new user
    def post(self, request):
        serializer = ActivateAccountSerializer(data=request.query_params)
        validate_serializer(serializer=serializer)
        # Update is_active property
        serializer.update(instance=serializer.validated_data)
        return Response({
            'success': True
        })


class ForgotPassword(APIView):
    permission_classes = (AllowAny,)

    # Send email forgot password
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        validate_serializer(serializer=serializer)
        serializer.save()
        return Response({
            'success': True
        })

    # Validate token
    def put(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        validate_serializer(serializer=serializer)
        # calls function serializer.validate() and save results in serializer.validated_data
        user, password = serializer.validated_data
        # Reset password
        serializer.update(instance=user, validated_data=password)
        return Response({
            'success': True
        })


class ChangePassword(APIView):
    # Update password
    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        validate_serializer(serializer=serializer)
        # calls function serializer.validate() and save results in serializer.validated_data
        user, password = serializer.validated_data
        # Reset password
        serializer.update(instance=user, validated_data=password)
        return Response({
            'success': True
        })
