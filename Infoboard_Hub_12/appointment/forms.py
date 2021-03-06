from django import forms
from django.contrib.auth.forms import  AuthenticationForm

from .models import Appointment, Advertising, Group

class AppointmentForm(forms.ModelForm):
 
    class Meta:
        model = Appointment
        fields = ( 'party_type', 'party_organizer' , 'group' , 'location','room', 'party_date')

        labels= { 
            'party_type': 'Veranstaltung', 
            'party_organizer': 'Veranstalter',
            'group': 'Berufsgruppe',
            'location': 'Ort',
            'party_date': 'Datum,Urzeit',
            'room': 'Room'
            }

        widgets = {
            'party_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Veranstaltung"}),
            'party_organizer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Veranstalter"}),
            'group': forms.Select(attrs={'class': 'form-control', 'placeholder': "Berufsgruppe"}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ort"}),
            'room': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Room"}),
            'party_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
            }


class AdvertisingForm(forms.ModelForm):
 
    class Meta:
        model = Advertising
        fields = ( 'title', 'body', 'image')
      
        labels= { 
            'title': 'Betreff', 
            'body': 'Details',
            'image': 'Werbebild',
            }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Betreff"}),
            'body': forms.Textarea(attrs={'class': 'form-control', 
                                            'placeholder': "Details" , 'style':'resize: none;'}), 
            'image': forms.FileInput(attrs={'type':"file" , 'class': 'form-control'}),
            }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label= "Benutzername" , 
        widget=forms.TextInput(attrs= {'class': 'form-control', 'placeholder':"Benutzername"}),
    )

    password = forms.CharField(
        label= "Kennwort" ,
        strip=False,
        widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': "Kennwort"}),
    )


class GroupForm(forms.ModelForm):
 
    class Meta:
        model = Group
        fields = ( 'name', )
      
        labels= {'name': 'Name'}

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Betreff"}),
            }    