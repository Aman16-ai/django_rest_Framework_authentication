from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200);
    completed = models.BooleanField(default=False, blank=True,null=True)
    
    def __str__(self):
        return self.title
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    education = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.first_name