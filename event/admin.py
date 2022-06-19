from django.contrib import admin
from .models import Event, Donation, Comment, VolunteerList
# Register your models here.

admin.site.register(Donation)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(VolunteerList)
