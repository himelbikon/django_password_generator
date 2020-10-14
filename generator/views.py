from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    str = 'abcdefghijklmnopqstuvwxyz'
    alphabates = list(str)
    thepassword = ''

    if request.GET.get('uppercase'):
        alphabates.extend(list(str.upper()))
    if request.GET.get('numbers'):
        alphabates.extend(list('0123456789'))
    if request.GET.get('special'):
        alphabates.extend(list('!@#$%^&*'))

    length = int(request.GET.get('length', 12))
    for x in range(length):
        thepassword += random.choice(alphabates)


    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
