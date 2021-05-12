from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import ComplaintSerializer, ComplaintDetailSerializer
from app.permissions.complaint import ComplaintPermission
from app.utils.serializer_validator import validate_serializer


class Complaint(APIView):
    permission_classes = (ComplaintPermission,)

    # List complaints
    def get(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        self.check_permissions(request=request)
        complaints = hotel.complaints.all()
        return Response({
            'success': True,
            'complaints': ComplaintDetailSerializer(complaints, many=True).data
        })

    # Create complaint
    def post(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        serializer = ComplaintSerializer(data=request.data, context={'user': request.user, 'hotel': hotel})
        self.check_permissions(request=request)
        validate_serializer(serializer=serializer)
        complaint = serializer.save()
        return Response({
            'success': True,
            'complaint': ComplaintDetailSerializer(complaint).data
        })


class ComplaintDetail(APIView):
    permission_classes = (ComplaintPermission,)

    # Get one complaint
    def get(self, request, hotel_id, complaint_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        complaint = models.Complaint.objects.get(uuid=complaint_id, hotel_id=hotel.uuid)
        return Response({
            'success': True,
            'complaint': ComplaintDetailSerializer(complaint).data
        })

    # Delete complaint
    def delete(self, request, hotel_id, complaint_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        complaint = models.Complaint.objects.get(uuid=complaint_id, hotel_id=hotel.uuid)
        # self.check_object_permissions(request=request, obj=complaint)
        complaint.delete()
        return Response({
            'success': True,
            'complaint': ComplaintDetailSerializer(complaint).data
        })