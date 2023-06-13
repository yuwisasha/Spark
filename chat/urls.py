from django.urls import path

from . import views

urlpatterns = [
    path('swipe',
         views.SwipeRightView.as_view(),
         name='swipe_right'),
    path('chat/<int:pk>',
         views.ChatView.as_view(),
         name='chat'),
]
