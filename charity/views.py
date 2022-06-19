from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.conf import settings
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin
from .models import Donations
from .models import Event
from .forms import DonationForm

import stripe

def donate(request):
    """ A view to return the donation page """
    return render(request, 'charity/charity.html')

def makedonations(request):
    """ A view to return the donation page 
    and handle all donations"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            donor.stripe_pid = pid
            donor.user = request.user
            donor.save()
            messages.info(request, 'Successfully made a donation')
            return redirect(reverse('donate'))
        else:
            messages.error(request, 'Sorry we cannot add Donation. \
                                Please ensure all fields are completed.')
    else:
        form = DonationForm()

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
                    amount=request.POST.get('amount'),
                    currency=settings.STRIPE_CURRENCY,
                )
    template = 'charity/donate.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)