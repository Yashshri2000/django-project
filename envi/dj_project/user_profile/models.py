from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pofile_pics')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    phone = models.IntegerField()
    
    def __strt__(self):
        return f'{self.user.username} Profile'