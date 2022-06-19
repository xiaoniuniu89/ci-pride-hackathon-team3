from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .forms import EventForm, CommentForm
from .models import Event, Donation, Comment, VolunteerList

class EventListView(ListView):
    """ list view of all events """
    paginate_by = 8
    now = datetime.now()
    date_today = now.date()
    queryset = Event.objects.filter(date__gte=date_today).order_by('-created')
    context_object_name = 'events'

def eventDetail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    comments = Comment.objects.filter(event=event)
    return render(request, 'event/event_detail.html', {'event': event, 'comments': comments})

@login_required
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
            VolunteerList.objects.create(event=event)
            return redirect('event_list')

    else:
        form = EventForm()


    return render(request, 'event/event_form.html', {'form': form})

    

class EventUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    update event
    """

    model = Event
    form_class = EventForm
    success_message = 'updated!'

    def get_success_url(self, **kwargs):
        slug = self.kwargs['slug']
        return reverse('event_detail', kwargs={'slug': slug})
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.organizer:
            return True
        return False

def deleteEvent(request):
    if request.POST.get('action') == 'delete-event':
        event_pk = request.POST.get('event_pk')
        event = Event.objects.get(pk=event_pk)
        event.delete()
        return JsonResponse({'msg': 'Your event was deleted'})

def createComment(request, pk):
    if request.method == 'POST':
        event = Event.objects.get(pk=pk)
        Comment.objects.create(event=event, user=request.user, body=request.POST.get('comment_body').lstrip().rstrip())
        return redirect('event_detail', event.slug )

def deleteComment(request):
    if request.POST.get('action') == 'delete':
        comment_pk = request.POST.get('comment_pk')
        event_pk = request.POST.get('event_pk')
        event = Event.objects.get(pk=event_pk)
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return JsonResponse({'msg': 'Your comment was deleted'})

def updateComment(request):
    if request.POST.get('action') == 'update':
        comment_pk = request.POST.get('comment_pk')
        comment_body = request.POST.get('comment_body')
        comment = Comment.objects.get(pk=comment_pk)
        comment.body = comment_body
        comment.save()
        return JsonResponse({'msg': 'Your comment was updated'})

def volunteer(request):

    if request.POST.get('action') == 'volunteer':
        event_pk = request.POST.get('event_pk')
        event = Event.objects.get(pk=event_pk)
        vl = VolunteerList.objects.get(event=event)
        vl.volunteers.add(request.user.id)
        return JsonResponse({'msg': 'You were added to the list of volunteers'})