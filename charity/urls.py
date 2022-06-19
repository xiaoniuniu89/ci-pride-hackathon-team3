from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('make-donation/', views.makedonations, name="make-donation"),
    path('success/', views.donationmade, name="done-donation"),
    path('donation/<int:pk>/', views.stripe_donation, name="make_donation"),
    path('webhook/', views.stripe_webhook),
]
