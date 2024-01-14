from django.db import models
from datetime import datetime
from django.urls import reverse


class Appointment(models.Model):
    date = models.DateField(default=datetime.utcnow,)
    client_name = models.CharField(max_length=100)
    message = models.TextField()

    def get_absolute_url(self):
        return reverse('appointment', args=[str(self.id)])

    def __str__(self):
        return f'{self.client_name}: {self.message}'
