from django import forms
from django.contrib.auth.forms import  AuthenticationForm

from .models import Appointment, Advertising

class AppointmentForm(forms.ModelForm):
 
    class Meta:
        model = Appointment
        fields = ( 'party_type', 'party_organizer' , 'group' , 'location', 'party_date')

        labels= { 
            'party_type': 'Party Type', 
            'party_organizer': 'Party Organizer',
            'group': 'Group',
            'location': 'Location',
            'party_date': 'Party Date',
            }

        widgets = {
            'party_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Type of party"}),
            'party_organizer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "The party organizer"}),
            'group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "The group invited to the party"}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Location of the party"}),
            'party_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
            }


class AdvertisingForm(forms.ModelForm):
 
    class Meta:
        model = Advertising
        fields = ( 'title', 'body', 'image')
      
        labels= { 
            'title': 'Advertising title', 
            'body': 'Advertising body',
            'image': 'Advertising image',
            }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Title of the Advertising"}),
            'body': forms.Textarea(attrs={'class': 'form-control', 
                                            'placeholder': "Write your Body of the Advertising here" , 'style':'resize: none;'}), 
            'image': forms.FileInput(attrs={'type':"file" , 'class': 'form-control'}),
            }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label= "Username" , 
        widget=forms.TextInput(attrs= {'class': 'form-control', 'placeholder':"username"}),
    )

    password = forms.CharField(
        label= "Password" ,
        strip=False,
        widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': "password"}),
    )



    