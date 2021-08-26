
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.db import connection

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", include ('appointment.urls')),  
]


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns+= staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


from appointment.models import Advertising
from appointment.views import AdvertisingUpdate

all_tables = connection.introspection.table_names()

if "appointment_advertising" in  all_tables:

    advertising_instance = Advertising.get_solo()
    urlpatterns.append(
        path('advertising/<int:pk>/update', AdvertisingUpdate.as_view(), name='advertising-update'))

