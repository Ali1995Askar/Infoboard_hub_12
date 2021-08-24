
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-dashboard', views.admin_dashboard, name='dashboard'),

    path('appointment/create', views.AppointmentCreate.as_view(), name='create'),
    path('appointment/<int:pk>/update', views.AppointmentUpdate.as_view(), name='update'),
    path('appointment/<int:pk>/delete', views.AppointmentDelete.as_view(), name='delete'),

   
    

  
]


