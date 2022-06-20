from datetime import datetime
from django.shortcuts import render

from event.models import Event

# Create your views here.
def index(request):
    """ A view to return the index page """
    now = datetime.now()
    date_today = now.date()
    event = Event.objects.all().exclude(pk=48).exclude(pk=45).exclude(pk=46).exclude(pk=47).order_by('-date')[:3]

    context = {
        'event': event 
    }
    return render(request, 'home/index.html', context)
