from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

class Post(models.Model):
    post_filter_choices = [
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JavaScript', 'JavaScript'),
        ('Python', 'Python'),
        ('React', 'React'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    post_filter = models.CharField(
        max_length=32, choices=post_filter_choices, default='HTML'
    )
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq.png', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

@receiver(post_save, sender=Post)
def create_post_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.owner,
            sender=instance.owner,
            content_type=ContentType.objects.get_for_model(Post),
            object_id=instance.id,
            content_object=instance,
            notification_type='post'
        )
    else:
        Notification.objects.create(
            recipient=instance.owner,
            sender=instance.owner,
            content_type=ContentType.objects.get_for_model(Post),
            object_id=instance.id,
            content_object=instance,
            notification_type='edit'
        )