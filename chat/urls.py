from django.urls import path

from . import views

urlpatterns = [
    path('swipe',
         views.SwipeRightView.as_view(),
         name='swipe_right'),
]
