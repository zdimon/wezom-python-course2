from django.urls import path
from contacts.views import contact_form

urlpatterns = [
    path('contact-us', contact_form, name='contact_form')
]
