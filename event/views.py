from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import (
    ListView,
    UpdateView
)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .forms import EventForm
from .models import Event, Donation, Comment

class EventListView(ListView):
    """ list view of all events """
    queryset = Event.objects.all()
    context_object_name = 'events'

def eventDetail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    comments = Comment.objects.filter(event=event)
    return render(request, 'event/event_detail.html', {'event': event, 'comments': comments})


def eventCreate(request):
    """create event view"""

    if request.method == 'POST':
        form = EventForm(data=request.POST)

        if form.is_valid():
            
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            Donation.objects.create(event=event)
            messages.success(request, f'created')
           
            return redirect('event_list')

    else:
        form = EventForm()


    return render(request, 'event/event_form.html', {'form': form})

    

class EventUpdateView(SuccessMessageMixin, UpdateView):
    """
    update event
    """

    model = Event
    form_class = EventForm
    success_message = 'updated!'

    def get_success_url(self, **kwargs):
        slug = self.kwargs['slug']
        
        return reverse('event_detail', kwargs={'slug': slug})

def eventDelete(request, pk):
    """ delete event """
    if request.method=="POST":
        event = Event.objects.get(pk=pk)
        event.delete()
        messages.success(request, 'deleted')
        return redirect('event_list')

