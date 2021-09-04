

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-dashboard', views.admin_dashboard, name='dashboard'),
    path('appointment/create', views.AppointmentCreate.as_view(), name='create'),
    path('appointment/<int:pk>/update', views.AppointmentUpdate.as_view(), name='update'),
    path('appointment/<int:pk>/delete', views.AppointmentDelete.as_view(), name='delete'),
    

    path('groups-dashboard', views.groups_dashboard, name='groups-dashboard'),
    path('group/create', views.GroupCreate.as_view(), name='group-create'),
    path('group/<int:pk>/update', views.GroupUpdate.as_view(), name='group-update'),
    path('group/<int:pk>/delete', views.GroupDelete.as_view(), name='group-delete'),


    path('admin-login/', views.admin_login, name='admin-login'),
    path('admin-logout/', views.admin_logout, name='admin-logout'),
 
]


