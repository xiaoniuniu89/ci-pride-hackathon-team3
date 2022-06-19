from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    profile
)

urlpatterns = [
    path('', profile, name='profile'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='user_profile/change-password.html')),
]