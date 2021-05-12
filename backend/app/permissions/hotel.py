from app.models import Role
from rest_framework.permissions import IsAuthenticated


# Permission for hotel api
class HotelPermission():
    def has_permission(self, request, view):
        # Get method for all roles, otherwise role hotelier
        if request.method == 'GET':
            return True
        else:
            return request.user.role == Role.HOTELIER

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
