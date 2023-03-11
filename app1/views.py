from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
def abc(request):
    return HttpRequest('abc movie') 
    