from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='default_profile_qdjgyp'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        name = instance.username  
        default_image_path = 'images/default_profile_qdjgyp.jpg'

        if not Profile.objects.filter(owner=instance).exists():
            profile = Profile.objects.create(owner=instance, name=name, image=default_image_path)

post_save.connect(create_profile, sender=User)