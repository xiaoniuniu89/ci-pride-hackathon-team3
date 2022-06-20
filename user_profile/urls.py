from django.urls import path
from .views import (
    profile,
    mail_volunteer_list
)

urlpatterns = [
    path('', profile, name='profile'),
    path('mail/', mail_volunteer_list, name='email_volunteers'),
]
