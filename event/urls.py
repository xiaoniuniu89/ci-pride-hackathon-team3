from django.urls import path
from .views import (
    EventListView,
    eventDetail,
    eventCreate,
    EventUpdateView,
    eventDelete
)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('<str:slug>/', eventDetail, name='event_detail'),
    path('new-event', eventCreate, name='event_create'),
    path('new-event', eventCreate, name='event_create'),
    path('update/<str:slug>/', EventUpdateView.as_view(), name='event_update'),
    path('delete/<int:pk>/', eventDelete, name='event_delete'),
]