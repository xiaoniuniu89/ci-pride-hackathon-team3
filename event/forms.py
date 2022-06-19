from django import forms

from .models import Event, Comment


class DatePicker(forms.DateInput):
    """
    date widget
    """
    input_type = 'date'
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])


class TimePicker(forms.TimeInput):
    """
    time widget
    """

    input_type = 'time'


class EventForm(forms.ModelForm):
    """
    for creating and updating events
    """

    class Meta:
        model = Event
        exclude = ('organizer', 'slug', 'volunteer_list')

        widgets = {
            'date': DatePicker(),
            'time': TimePicker(),
        }


class CommentForm(forms.ModelForm):
    """comment form """
    model = Comment
    fields = ['body']

    widgets = {
        'body': forms.TextInput(attrs={'class': 'form-control'})
    }
