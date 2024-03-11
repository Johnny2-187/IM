from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.user.username
