from django import forms
from .models import Donations


class DonationForm(forms.ModelForm):
    """ Form to allow users to add donations """
    class Meta:
        model = Donations
        fields = '__all__'
