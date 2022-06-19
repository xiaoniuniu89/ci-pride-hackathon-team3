from event.models import Event, Donation

from django.core.exceptions import ObjectDoesNotExist

def payment_confirmation(pk, amount):
    """ post webhook payment confirmation view """
    # find event and make a donation 
    event = Event.objects.get(pk=pk)
    amount = amount // 100
    donation = Donation.objects.get(event=event)
    donation.total += amount
    donation.save()
    print('donation updated')

   