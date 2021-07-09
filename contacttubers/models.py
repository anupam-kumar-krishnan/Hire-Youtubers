from django.db import models
from datetime import datetime
# Create your models here.
class Contacttuber(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateField(blank=True, default=datetime.now)

def __str__(self):
        return self.full_name