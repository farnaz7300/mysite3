from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm , ContactForm
from django.contrib import messages


def index_view(request):
    return render(request,('website/index.html'))
def about_view(request):
    return render(request,('website/about.html'))
def contact_view(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submit successfully')
    else:
        messages.add_message(request,messages.ERROR,'your ticket didnt submited')
    return render(request,('website/contact.html'))
# Create your views here.
