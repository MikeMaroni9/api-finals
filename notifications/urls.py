from django.urls import path, include
from .views import NotificationList

urlpatterns = [
    path('api/notifications/', NotificationList.as_view(), name='notification-list'),
]