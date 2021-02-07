from django.contrib.auth.models import User
from django.db import models
from posts.models import Post
from django.utils import timezone


class Comments(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(timezone.now)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name
