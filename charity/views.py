from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.csrf import csrf_exempt

from .models import Donations
from .models import Event
from .forms import DonationForm
from .utils import payment_confirmation

from event.models import Event
import stripe
import json
import os 
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@login_required
def stripe_donation(request, pk):
    """stripe donation"""
    if request.method == 'POST':
        amount = request.POST.get('amount')
        amount = int(amount) * 100
        event = Event.objects.get(pk=pk)
        # create payment intent with stripe
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='eur',
            automatic_payment_methods={
                'enabled': True,
            },
            # will use this later in webhook to update billing status
            metadata={'event_id': pk, 'user_id': request.user.pk}
        )
        print(f'{request.user} mad a donation of {amount} for {event.name}')
        return render(
        request,
        'charity/donate.html',
        {
            'client_secret': intent.client_secret,
            'intent': intent,
            'title': 'Donate'
        })


@csrf_exempt
def stripe_webhook(request):
    """listens for payment_intent.succeeded"""
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.metadata.event_id, event.data.object.metadata.user_id, event.data.object.amount)

    else:
        print(f'Unhandled event type {event.type}')

    return HttpResponse(status=200)


def donate(request):
    """ A view to return the donation page """
    template = 'charity/donate.html'
    
    return render(request, template)


def makedonations(request):
    """ A view to return the donation page
    and handle all donations"""

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.user = request.user
            donor.save()
            messages.info(request, 'Successfully made a donation')
            return redirect(reverse('done-donation'))
        else:
            messages.error(request, 'Sorry we cannot add Donation. \
                                Please ensure all fields are completed.')
    else:
        form = DonationForm()

    template = 'charity/donate.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def donationmade(request):
    """ A view to thank users for donation """

    template = 'charity/success.html'
    return render(request, template)
