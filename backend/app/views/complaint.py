from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import ComplaintSerializer, ComplaintDetailSerializer
from app.permissions.complaint import ComplaintPermission
from app.utils.serializer_validator import validate_serializer
from pusher import Pusher


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
        pusher = Pusher(app_id='1209674', key='5d873d3e35474aa76004', secret='ffcb966b2161f86209bc', cluster='ap1')
        message = {
            'success': True,
            'complaint': ComplaintDetailSerializer(complaint).data
        }
        pusher.trigger(u'a_channel', u'an_event_2', message)
        return Response(message)


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

    def put(self, request, hotel_id, complaint_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        complaint = models.Complaint.objects.get(uuid=complaint_id, hotel_id=hotel.uuid)
        # self.check_object_permissions(request=request, obj=review)
        serializer = ComplaintSerializer(data=request.data)
        validate_serializer(serializer=serializer)
        review = serializer.update(instance=complaint, validated_data=serializer.validated_data)
        return Response({
            'success': True,
            'review': ComplaintDetailSerializer(review).data
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