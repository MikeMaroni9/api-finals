from django.db.models.signals import post_save
from django.dispatch import receiver
from likes.models import Like 
from notifications.models import Notification
from django.contrib.auth.models import User
from django.core.signals import Signal

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    print("Signal received!")
    if created:
        print(f"Like created by {instance.owner} on post {instance.post}")
        Notification.objects.create(
            recipient=instance.post.owner,
            sender=instance.owner,
            post=instance.post,
            notification_type='like'
        )


