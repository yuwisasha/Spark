from django.urls import path

from . import views

urlpatterns = [
     path('create_user',
          views.RegisterUserView.as_view(),
          name='create_user'),
     path('create_profile',
          views.CreateProfileView.as_view(),
          name='create_profile'),
     path('user_list',
          views.UserListView.as_view(),
          name='user_list'),
     path('profile_list',
          views.ProfileListView.as_view(),
          name='profile_list'),
]
