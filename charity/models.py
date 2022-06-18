from django.db import models
from django.contrib.auth.models import User
from event.models import Event

class Donations(models.Model):
    SELECT = [
        (1, ' Consent Workshop'),
        (2, 'Outright International'),
        (3, 'Global Giving'),
        (4, 'Micro Rianbow'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=False, blank=False)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=0,
                                        null=False, default=0)
    charities = models.CharField(choices=SELECT, max_length=2)
    date = models.DateTimeField(auto_now_add= True)
    class Meta:
        verbose_name_plural = 'Donations'
        ordering = ['-date']

def __str__(self):
    return self.event_name
