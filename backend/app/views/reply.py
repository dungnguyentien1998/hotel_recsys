from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import ReplySerializer, ReplyDetailSerializer
from app.utils.serializer_validator import validate_serializer


class Reply(APIView):
    def post(self, request, complaint_id):
        complaint = models.Complaint.objects.get(uuid=complaint_id)
        serializer = ReplySerializer(data=request.data, context={'complaint': complaint})
        validate_serializer(serializer=serializer)
        reply = serializer.save()
        return Response({
            'success': True,
            'complaint': ReplyDetailSerializer(reply).data
        })

    def get(self, request):
        user = request.user
        complaints = models.Complaint.objects.filter(user_id=user.uuid)
        replys = []
        for complaint in complaints:
            reply = models.Reply.objects.filter(complaint_id=complaint.uuid)
            replys.append(reply)
        return Response({
            'success': True,
            'complaints': ReplyDetailSerializer(replys, many=True).data
        })
