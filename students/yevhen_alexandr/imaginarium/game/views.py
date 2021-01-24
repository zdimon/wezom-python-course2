from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from .models import Contact

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'game/index.html')


class ContactsView(View):
    def get(self, request):
        return render(request, 'game/contacts.html')

    def post(self, request):
        contact = Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        contact.save()

        return redirect(ContactsView.as_view())