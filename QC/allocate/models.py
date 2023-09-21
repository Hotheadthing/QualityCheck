from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class QCProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

class Assignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    qc_person = models.ForeignKey(QCProfile, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

