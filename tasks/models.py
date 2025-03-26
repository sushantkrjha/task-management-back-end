from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=[("Work", "Work"), ("Personal", "Personal"), ("Urgent", "Urgent")], default="Work")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
