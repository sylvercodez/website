from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    base_image = Base.objects.all()
    contacts = Contact.objects.all()
    portfolio = Portfolio.objects.all()

    abouts = About.objects.all()
    context = {'base_image':base_image,'contact': contacts,'portfolio': portfolio,'abouts':abouts}
    return render(request, 'index.html',context)
