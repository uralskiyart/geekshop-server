from django.urls import path

import users.views
from users.views import UserLoginView, UserRegistrationView, UserLogoutView, UserProfileView, UserVerifyView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('verify/<email>/<activation_key>/', UserVerifyView.verify, name='verify'),
]