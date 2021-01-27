from django.shortcuts import render
from contacts.models import Contact
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse


def contact_form(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.save()
        messages.success(request, 'Thank you!')
        return redirect(reverse('contact_form'))
    return render(request, 'contacts/index.html')
