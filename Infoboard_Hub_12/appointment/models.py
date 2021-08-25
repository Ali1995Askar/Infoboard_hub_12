from django.db import models
from solo.models import SingletonModel

class Appointment(models.Model):
    party_type = models.CharField(max_length=250) 
    party_organizer = models.CharField(max_length=250) 
    group = models.CharField(max_length=250) 
    location = models.CharField(max_length=250) 
    party_date =  models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.party_type + " organized by " + self.party_organizer + " on " + str(self.party_date)


class Advertising (SingletonModel):
    singleton_instance_id = 1
    title = models.CharField(max_length=250,  default='Hello every one') 
    body = models.TextField(default='welcom to the party wish you all the best, have a nice day')
    image = models.ImageField(upload_to='advertising-images/', default='logo.jpg', null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 