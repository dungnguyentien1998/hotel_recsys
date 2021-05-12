from app.models import Hotel, Room, Role
from app.permissions import HotelierPermission


# Permission for room api
class RoomPermission(HotelierPermission):
    def has_permission(self, request, view):
        # Get method for all user, otherwise role hotelier
        if request.method == 'GET':
            return True
        else:
            return request.user.role == Role.HOTELIER

    def has_object_permission(self, request, view, obj):
        # Only user who owns a hotel can modify rooms of that hotel
        if isinstance(obj, Hotel):
            return request.user == obj.user
        elif isinstance(obj, Room):
            return request.user == obj.hotel.user
        else:
            return False
