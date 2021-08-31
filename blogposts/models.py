from django.contrib import auth
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', args=[str(self.id)])

class Comment(models.Model):
    blogpost = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments',
        )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.comment

    def get_absolute_url(self):
        return reverse('blogpost_list')