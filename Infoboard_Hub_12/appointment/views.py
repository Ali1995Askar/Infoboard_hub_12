from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Appointment, Advertising
from .forms import AppointmentForm, AdvertisingForm, LoginForm

# Create your views here.

def index(request):
    appointments = Appointment.objects.all()
    advertising = Advertising.get_solo()
    return render(request, 'index.html', context={'appointments': appointments, 'advertising': advertising}) 


def admin_login(request):

    if request.method =='POST':
            login_form = LoginForm(data = request.POST)
            if login_form.is_valid():
              
                #login user
                user = login_form.get_user()
                login(request , user)
                return redirect ('/admin-dashboard' )
            else:
                context = {'form' : login_form}
                return  render (request , 'login.html' , context )
    else:
        login_form = LoginForm ()
        context = {'form' : login_form}
        return  render (request , 'login.html' , context )


@login_required (login_url = 'admin-login')
def admin_logout (request) :
        logout (request)
        return redirect ('/' )


@login_required (login_url = 'admin-login')
def admin_dashboard(request):
    if request.method =='POST':
        advertising_form = AdvertisingForm(request.POST)
        if advertising_form.is_valid():
            appointments = Appointment.objects.all()
            return render(request, 'admin_dashboard.html', context={'appointments': appointments, 'form': advertising_form }) 
    else:
        advertising_form = AdvertisingForm()
        appointments = Appointment.objects.all()

        return render(request, 'admin_dashboard.html', context={'appointments': appointments, 'form': advertising_form }) 


@method_decorator(login_required(login_url = 'admin-login'), name='dispatch')
class AppointmentCreate(CreateView):
    login_required = True
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
   
    def get_success_url(self):
          return reverse('dashboard')


@method_decorator(login_required(login_url = 'admin-login'), name='dispatch')
class AppointmentUpdate(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
    context_object_name = 'appointment'
  

    def get_success_url(self):
        return reverse('dashboard')


@method_decorator(login_required(login_url = 'admin-login'), name='dispatch')
class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = 'delete_appointment.html'

    def get_success_url(self):
        return reverse('dashboard')


@method_decorator(login_required(login_url = 'admin-login'), name='dispatch')
class AdvertisingUpdate(UpdateView):
    model = Advertising
    form_class = AdvertisingForm
    template_name = 'advertising_form.html'

    def get_success_url(self):
        return reverse('index')
