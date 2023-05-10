from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class Supervisor(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="supervisor"
    )
    task = models.ManyToManyField(Task, related_name="tasks")
