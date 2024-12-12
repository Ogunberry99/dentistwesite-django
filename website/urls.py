from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name='home'),
path('contact.html', views.contact, name='contact'),
path('services.html', views.services, name='services'),
path('appointment.html', views.appointment, name='appointment'),
path('about.html', views.about, name='about'),
path('appointmentresult.html', views.appointmentresult, name='appointmentresult')
]