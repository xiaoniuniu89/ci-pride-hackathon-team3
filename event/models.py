from django.db import models
from django.contrib.auth.models import User
import uuid
from PIL import Image
# real time chat
# contacting the organizer - inbox for the event / group chat for volunteers  - users have an inbox
# comments


class Event(models.Model):
    """Model for events"""

    ConsentWorkshop = 'Consent Workshop'
    OutrightInternational = 'Outright International'
    GlobalGiving = 'Global Giving'
    MicroRainbow = 'Micro Rainbow'
    SELECT = [
        (ConsentWorkshop, 'Consent Workshop'),
        (OutrightInternational, 'Outright International'),
        (GlobalGiving, 'Global Giving'),
        (MicroRainbow, 'Micro Rainbow'),
    ]
    
    charity = models.CharField(choices=SELECT, max_length=22)
    name = models.CharField(max_length=50)
    featured_image = models.ImageField(default='default.jpg', upload_to='media')
    description = models.TextField()
    slug = models.SlugField(default=uuid.uuid4) # make unique
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50) # look in to cities
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    


    def __str__(self):
        return f'{self.organizer.username} event {self.name}'
    
    def get_donation_total(self):
        """ method to return donation total"""
        donation = Donation.objects.get(event_id=self.id)
        return donation.total
    
    # def save(self, *args, **kwargs):
    #     ## rescale images when uploaded 
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.featured_image.path)
    #     if img.height > 500 or img.width > 500:
    #         output_size = (500, 500)
    #         img.thumbnail(output_size)
    #         img.save(self.featured_image.path)


class VolunteerList(models.Model):
    volunteers = models.ManyToManyField(User)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=13)


class Donation(models.Model):
    """model for donation"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f'Donation for {self.event.name}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('updated', )

# class Volunteer(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
# pledge then -> the site asks for money 
# pledge - then pay

# donations build up

# target amount - 