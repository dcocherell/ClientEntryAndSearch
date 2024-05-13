from django.db import models
import datetime
from django.utils import timezone
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    STATUS_CHOICES = [
        ('#00FF00', 'Green'),
        ('#FFFF00', 'Yellow'),
        ('#FF0000', 'Red'),
        ('#964B00', 'Brown'),
        ('#000000', 'Black'),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    status = ColorField(choices=STATUS_CHOICES, default='#00FF00')
    notes = models.TextField(blank=True)
    services_rendered = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def clean_status(self):
            if self.status not in [choice[0] for choice in self.STATUS_CHOICES]:
                raise ValidationError(
                    _('Invalid color choice. Please select one of the predefined colors.'),
                    code='invalid_color'
                )