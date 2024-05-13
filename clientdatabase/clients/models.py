from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)