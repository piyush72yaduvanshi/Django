from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'website/index.html')

def contact(request):
    return HttpResponse("This is the contact page of Chaiaur Django.")

def services(request):
    return HttpResponse("This is the services page of Chaiaur Django.")