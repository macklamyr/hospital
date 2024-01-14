from django.shortcuts import render, reverse, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from datetime import datetime
from django.urls import reverse_lazy
from .filters import AppointmentFilter
from .models import Appointment
from .forms import AppointmentForm


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            message=appointment.message,
            from_email='HaibullinRamazan@yandex.ru',
            recipient_list=['ramazanhaibullin978@gmail.com', ]
        )

        return redirect('appointments:make_appointment')


class AppointmentList(ListView):
    model = Appointment
    ordering = 'client_name'
    template_name = 'appointments.html'
    context_object_name = 'appointments'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AppointmentFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AppointmentDetail(DetailView):
    model = Appointment
    template_name = 'appointment.html'
    context_object_name = 'appointment'


class AppointmentCreate(CreateView):
    form_class = AppointmentForm
    model = Appointment
    template_name = 'appointment_add.html'


class AppointmentUpdate(UpdateView):
    form_class = AppointmentForm
    model = Appointment
    template_name = 'appointment_add.html'


class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = 'appointment_delete.html'
    success_url = reverse_lazy('appointments')

