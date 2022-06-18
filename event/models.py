from django.db import models
from django.contrib.auth.models import User
import uuid
# real time chat
# contacting the organizer - inbox for the event / group chat for volunteers  - users have an inbox
# comments



class Event(models.Model):
    """Model for events"""

    name = models.CharField(max_length=50)
    featured_image = models.ImageField(default='default.jpg', upload_to='event_featured_images')
    description = models.TextField()
    slug = models.SlugField(max_length=255) # make unique
    slug_end = models.UUIDField(default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50) # look in to cities
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    volunteer_list = models.ManyToManyField(User, blank=True, related_name='volunteers')


    def __str__(self):
        return f'{self.organizer.username} event {self.name}'
    
    def get_donation_total(self):
        """ method to return donation total"""
        donation = Donation.objects.get(event_id=self.id)
        return donation.total

    def save(self, *args, **kwargs):
        # image_resize(self.featured_image, 512, 512)
        self.slug += f'-{self.slug_end}'
        super().save(*args, **kwargs)

    

class Donation(models.Model):
    """model for donation"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return f'Donation for {self.event.name}'

# class Volunteer(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
# pledge then -> the site asks for money 
# pledge - then pay

# donations build up

# target amount - 