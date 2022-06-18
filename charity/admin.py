from django.contrib import admin
from .models import Donations


class DonationsAdmin(admin.ModelAdmin):
    """ Display donations by user """
    list_display = (
        'user',
        'email',
        'amount',
        'date',
    )

    ordering = ('-date',)


admin.site.register(Donations, DonationsAdmin)
