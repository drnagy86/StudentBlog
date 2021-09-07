from django.contrib import auth
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.forms.widgets import HiddenInput
from django.urls import reverse

class Tag(models.Model):
    tag = models.CharField(max_length=25, unique=True)

    def __str__(self) -> str:
        return self.tag

class BlogPost(models.Model):
    # dash means in descending order
    class Meta:
        ordering = ('-created_on',)

    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(Tag, related_name='blogposts')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', args=[str(self.id)])


class Comment(models.Model):    
    class Meta:
        ordering = ('-created_on',)

    blogpost = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        
        related_name='comments',
        )
    comment = models.CharField(max_length=140)
    author = models.CharField(max_length=100, default='Anonymous')
    created_on = models.DateTimeField(auto_now = True)
    approved = models.BooleanField(default=False)



    def __str__(self) -> str:
        return self.comment

    def get_absolute_url(self):
        return reverse('blogpost_list')

    def save(self, force_insert=True, *args, **kwargs):
        

        # super().save(*args, force_insert=True, **kwargs)
        super().save(*args, **kwargs)