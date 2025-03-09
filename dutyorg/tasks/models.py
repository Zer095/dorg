from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name
    
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),        
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(default=timezone.now)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    urgent = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_tasks')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def get_priority_color(self):
        return {
            'low': 'info',
            'medium': 'warning',
            'high': 'danger'
        }.get(self.priority, 'secondary')