from django.shortcuts import render
from .models import Profile
from charity.models import Donations
from event.models import Event, VolunteerList
from event.forms import EventForm
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
# Create your views here.


def profile(request):
    profile = Profile.objects.get(user=request.user)
    events = Event.objects.filter(organizer=request.user)
    donations = Donations.objects.filter(user=request.user)
    return render(request, 'user_profile/profile.html', {'profile': profile, 'events': events, 'donations': donations})

def mail_volunteer_list(request):
    if request.POST.get('action') == 'email':
        event_pk = request.POST.get('event_pk')
        event = Event.objects.get(pk=event_pk)
        email_body = request.POST.get('email_body')
        print(email_body)
        vl_list = VolunteerList.objects.get(event=event)
        emails = [user.email for user in vl_list.volunteers.all()]
        for email in emails:
            message = render_to_string("email.html", {'message': email_body})
            mail = EmailMessage(
                subject=f"Update about {event.name}",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[email, ],
            )
            mail.content_subtype = "html"
            try:
                mail.send()
        
            except Exception:
                pass
        return JsonResponse({'msg': 'Your email was sent'})