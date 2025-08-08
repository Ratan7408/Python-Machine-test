from django.db import models
from django.contrib.auth.models import User
from clients.models import Client

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='assigned_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_created')
    
    def __str__(self):
        return self.project_name
    
    class Meta:
        ordering = ['-created_at']
