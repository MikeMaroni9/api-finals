from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    post_filter_choices = [
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('javascript', 'JavaScript'),
        ('python', 'Python'),
        ('react', 'React'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    post_filter = models.CharField(
        max_length=32, choices=post_filter_choices, default='normal'
    )
    image = models.ImageField(
        upload_to='images/', default='https://res.cloudinary.com/dyv1fobjp/image/upload/v1698973587/default_post_rgq6aq.png', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'