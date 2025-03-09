from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Extra fields
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    timezone = models.CharField(max_length=50, default='UTC')

    # Replace username with email for login
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email