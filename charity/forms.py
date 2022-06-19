from django import forms
from .models import Donations


class DonationForm(forms.ModelForm):
    """ Form to allow users to add donations """
    class Meta:
        model = Donations
        fields = ('email', 'event_name', 'amount', 'charities')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['charities'].label = "Select a charity for your choice"
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey rounded-0',
