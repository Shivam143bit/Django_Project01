from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bike(request):
    return HttpResponse('I love Hunter Royal Enfield Bike.')