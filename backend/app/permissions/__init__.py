from rest_framework.permissions import IsAuthenticated
from app.models.user import Role
from app.exceptions import Unauthenticated


# Permission for user
class UserPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request=request, view=view):
            raise Unauthenticated
        return request.user.role == Role.USER

    def has_object_permission(self, request, view, obj):
        super().has_object_permission(request=request, view=view, obj=obj)


# Permission for hotelier
class HotelierPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request=request, view=view):
            raise Unauthenticated
        return request.user.role == Role.HOTELIER

    def has_object_permission(self, request, view, obj):
        super().has_object_permission(request=request, view=view, obj=obj)


# Permission for admin
class AdminPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request=request, view=view):
            raise Unauthenticated
        return request.user.role == Role.ADMIN

    def has_object_permission(self, request, view, obj):
        super().has_object_permission(request=request, view=view, obj=obj)



