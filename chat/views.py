from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions, status

from .serializers import SwipeSirealizer, MessageSerializer
from .models import Swipe, Message


class SwipeRightView(generics.CreateAPIView):
    queryset = Swipe.objects.all()
    serializer_class = SwipeSirealizer


class ChatView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self, pk=None):
        user = self.request.user
        return Message.objects.filter(sender_id=user.id,
                                      receiver_id=pk)

    def list(self, request, pk):
        queryset = self.get_queryset(pk=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
