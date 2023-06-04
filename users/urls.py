from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('create_profile', views.CreateProfileView.as_view(), name='create_profile')
]
