from django.contrib import admin
from django.urls import path
from arduinoParcial import views as appv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lecturas_sensor/', appv.lecturas, name='lecturas_sensor')
]
