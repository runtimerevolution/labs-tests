
from django.db import models
from django.utils import timezone

from integrations.aws.s3.models import Picture


class User(models.Model):
    email = models.EmailField()
    name_first = models.CharField(max_length=100)
    name_last = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ForeignKey(Picture, on_delete=models.SET_NULL, related_name='user', null=True, blank=True)
    profile_picture_updated_at = models.DateTimeField(null=True, blank=True)
    user_handle = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_first + ' ' + self.name_last