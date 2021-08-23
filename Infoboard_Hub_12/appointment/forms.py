from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
 
    class Meta:
        model = Appointment
        fields = ( 'party_type', 'party_organizer' , 'group' , 'location', 'party_date')
      
