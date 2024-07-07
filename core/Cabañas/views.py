from django.shortcuts import render
from .models import Contact


# Create your views here.
def base (request):
    return render(request, "core/base.html")

def acerca(request):
    return render(request, "core/acerca.html")

def contact(request):
    return render(request, "core/contact.html")

def terminos(request):
    return render(request, "core/terminos.html")

def List_Contact(request):
    contacts=Contact.objects.all()
    return render(request, "contact.html", {'contacts':contacts})

# Create your views here.
