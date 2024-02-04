from django.db.models.signals import post_save
from django.dispatch import receiver
from likes.models import Like
from notifications.models import Notification
from django.contrib.auth.models import User

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.owner,
            sender_profile_id=instance.owner.profile.id,
            post=instance.post,
            notification_type='like'
        )