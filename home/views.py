from datetime import datetime
from django.shortcuts import render

from event.models import Event

# Create your views here.
def index(request):
    """ A view to return the index page """
    now = datetime.now()
    date_today = now.date()
    event = Event.objects.all().order_by('-date')[:3]

    context = {
        'event': event 
    }
    return render(request, 'home/index.html', context)
