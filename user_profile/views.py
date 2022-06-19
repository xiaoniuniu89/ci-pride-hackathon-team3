from django.shortcuts import render
from .models import Profile
from charity.models import Donations
from event.models import Event
# Create your views here.


def profile(request):
    profile = Profile.objects.get(user=request.user)
    events = Event.objects.filter(organizer=request.user)
    donations = Donations.objects.filter(user=request.user)
    print(donations)
    return render(request, 'user_profile/profile.html', {'profile': profile, 'events': events, 'donations': donations})