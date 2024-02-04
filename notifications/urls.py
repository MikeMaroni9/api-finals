from django.urls import path
from .views import NotificationList

urlpatterns = [
    path('api/notifications/', NotificationList.as_view(), name='notification-list'),
]