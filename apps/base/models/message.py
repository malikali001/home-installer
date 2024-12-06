from django.db import models
from django.utils import timezone

from .custom_user import CustomUser
from .query import Query


class Message(models.Model):
    content = models.TextField(blank=True, null=True)
    file = models.ImageField(upload_to='message_files/', blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=25)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name="queries")
