from django.db.models.signals import post_save
from django.dispatch import receiver
from likes.models import Like  # Import your Like model
from notifications.models import Notification

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.owner,
            sender=instance.owner,
            post=instance.post,
            notification_type='like'
        )