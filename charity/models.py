from django.db import models
from django.contrib.auth.models import User
from event.models import Event


class Donations(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    
    date = models.DateTimeField(auto_now_add= True)
    class Meta:
        verbose_name_plural = 'Donations'
        ordering = ['-date']

def __str__(self):
    return self.event_name
