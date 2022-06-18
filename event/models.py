from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    """Model for events"""

    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.organizer.username} event {self.name}'
    
    def get_donation_total(self):
        """ method to return donation total"""
        donation = Donation.objects.get(event_id=self.id)
        return donation.total
    

class Donation(models.Model):
    """model for donation"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return f'Donation for {self.event.name}'