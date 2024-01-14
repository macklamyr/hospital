from django import forms
from .models import Appointment
from django.core.exceptions import ValidationError


class AppointmentForm(forms.ModelForm):
    message = forms.CharField(min_length=5)

    class Meta:
        model = Appointment
        fields = [
            'client_name',
            'message',
        ]

    def clean(self):
        cleaned_data = super().clean()
        message = cleaned_data.get("message")
        client_name = cleaned_data.get("client_name")
        if client_name == message:
            raise ValidationError(
                "Описание не должно быть идентичным имени."
            )

        return cleaned_data
