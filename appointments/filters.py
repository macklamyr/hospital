from django_filters import FilterSet
from .models import Appointment


class AppointmentFilter(FilterSet):
    class Meta:
        model = Appointment
        fields = {
            'client_name': ['icontains'],
            'message': ['icontains'],
        }
