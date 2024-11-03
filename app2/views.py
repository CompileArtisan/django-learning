from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_bye(request):
    return HttpResponse('<marquee>bye bye bye peepl </marquee>')

def say_buhbye(request):
    return render(request, 'buhbye.html', {'name': 'Praanesh'})

def home(request):
    return HttpResponse('go somewhere')
