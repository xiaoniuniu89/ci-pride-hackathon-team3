from django.contrib import admin
from .models import Donations


class DonationsAdmin(admin.ModelAdmin):
    """ Display donations by user """
    list_display = (
        'user',
        'amount',
    )

    ordering = ('-date',)


admin.site.register(Donations, DonationsAdmin)
