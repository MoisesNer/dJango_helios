from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    options = (
        ('draft', 'Draft'),
        ('publised', 'Publised')
    )

    title = models.CharField(max_length=250)
#  SLUG is wat you will see in the address bar
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publised = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, default='draft', choices=options)