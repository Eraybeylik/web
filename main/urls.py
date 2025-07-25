from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('services/work-permit/', views.service_work_permit, name='service_work_permit'),
    path('services/residence-permit/', views.service_residence_permit, name='service_residence_permit'),
    path('services/citizenship/', views.service_citizenship, name='service_citizenship'),
    path('contact/', views.contact, name='contact'),
]