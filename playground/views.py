from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hey(request):
    return HttpResponse('''
                        <h1>
                            Hey there! I am using WhatsApp.
                        </h1>
                        ''')