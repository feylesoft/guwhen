from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request,'services.html')

def kurumsal(request):
    return render(request,'kurumsal.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    return render(request, 'contact.html')