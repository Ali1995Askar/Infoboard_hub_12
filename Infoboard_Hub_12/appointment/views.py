from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Appointment
from .forms import AppointmentForm

# Create your views here.

def index(request):
    appointments = Appointment.objects.all()
    return render(request, 'index.html', context={'appointments': appointments}) \


def admin_dashboard(request):
    appointments = Appointment.objects.all()
    return render(request, 'admin_dashboard.html', context={'appointments': appointments}) 


class AppointmentCreate(CreateView):
    login_required = True
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
   
    def get_success_url(self):
          return reverse('dashboard')


class AppointmentUpdate(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
    context_object_name = 'appointment'
  

    def get_success_url(self):
        return reverse('dashboard')


class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = 'delete_appointment.html'

    def get_success_url(self):
        return reverse('dashboard')
