from django.db import models
import uuid
from django.contrib.auth.models import User



class Generator(models.Model):
    id = models.UUIDField(
            primary_key=True, 
            default=uuid.uuid4, 
            editable=False)
    username = models.CharField(max_length=30)
    site = models.CharField(max_length=40)
    password = models.BinaryField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.username
