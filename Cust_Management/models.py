from django.db import models
from django.utils import timezone

# from simplemathcaptcha.fields import MathCaptchaField
# Create your models here.

class Employee(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    

   
    def __str__(self):
        return self.first_name+' '+self.last_name