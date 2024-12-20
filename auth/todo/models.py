from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255,null=True)
    users = models.ForeignKey(
        "User", on_delete=models.CASCADE, null=True, blank=True
    )    
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
