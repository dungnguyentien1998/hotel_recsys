from app.models import Role
from app.permissions import UserPermission


# Permission for booking api
class BookingPermission(UserPermission):
    def has_permission(self, request, view):
        # Get method for all roles, otherwise role user
        if request.method == 'GET':
            return True
        else:
            return request.user.role == Role.USER

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
