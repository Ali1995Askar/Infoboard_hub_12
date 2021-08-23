from django.db import models


class Appointment(models.Model):
    party_type = models.CharField(max_length=250) 
    party_organizer = models.CharField(max_length=250) 
    group = models.CharField(max_length=250) 
    location = models.CharField(max_length=250) 
    party_date =  models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.party_type + " organized by " + self.party_organizer + " on " + str(self.party_date)

