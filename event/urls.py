from django.urls import path
from .views import (
    EventListView,
    eventDetail,
    eventCreate,
    EventUpdateView,
    EventDeleteView,
    createComment,
    deleteComment,
    updateComment
)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('new-event/', eventCreate, name='event_create'),
    path('<str:slug>/', eventDetail, name='event_detail'),
    path('update/<str:slug>/', EventUpdateView.as_view(), name='event_update'),
    path('delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),
    path('create-comment/<int:pk>/', createComment, name='comment_create'),
    path('comment/delete/', deleteComment, name='comment_delete'),
    path('comment/update/', updateComment, name='comment_update'),
]