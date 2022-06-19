from event.models import Event, Donation
from .models import Donations

from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

def payment_confirmation(pk, user_pk, amount):
    """ post webhook payment confirmation view """
    # find event and make a donation 
    event = Event.objects.get(pk=pk)
    amount = amount // 100
    print(amount)
    donation = Donation.objects.get(event=event)
    donation.total += amount
    donation.save()
    user = User.objects.get(pk=user_pk)
    Donations.objects.create(event=event, user=user, amount=amount)
    print('donation updated')

   