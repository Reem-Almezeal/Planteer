from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .forms import ContactForm
from .models import Contact
from plants.models import Plant


def home_view(request:HttpRequest):
    featured_plants = Plant.objects.all().order_by('-created_at')[:4]
    return render(request, 'core/home.html', {
        'featured_plants': featured_plants
    })

def about_view(request:HttpRequest):
    return render(request, 'core/about.html')

def services_view(request:HttpRequest):
    return render(request, 'core/services.html')


def contact_view(request:HttpRequest):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            success = True
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form,
        'success': success,
    })


def contact_messages_view(request:HttpRequest):
    messages = Contact.objects.all().order_by('-created_at')
    return render(request, 'core/contact_messages.html', {
        'messages': messages,
    })

def services_view(request:HttpRequest):
    return render(request, 'core/services.html')