from django.contrib import admin
from .models import Event, Donation
# Register your models here.

admin.site.register(Donation)
admin.site.register(Event)