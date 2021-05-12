from app.models import Role
from app.permissions import UserPermission


# Permission for complaint api
class ComplaintPermission():
    def has_permission(self, request, view):
        # Post method for role user, otherwise role hotelier
        if request.method == 'POST':
            return request.user.role == Role.USER
        else:
            return request.user.role == Role.HOTELIER

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
