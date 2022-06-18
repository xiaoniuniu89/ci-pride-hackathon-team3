from django.contrib import admin
from .models import Event, Donation
# Register your models here.


@admin.register(Event)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Donation)