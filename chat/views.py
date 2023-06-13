from rest_framework import generics
# from rest_framework.views import APIView

from .serializers import SwipeSirealizer, MessageSerializer
from .models import Swipe, Message


class SwipeRightView(generics.CreateAPIView):
    queryset = Swipe.objects.all()
    serializer_class = SwipeSirealizer
