from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def products(request):
    context = {}
    context['objects'] = Item.objects.all()
    return render(request, 'lol.html', context)