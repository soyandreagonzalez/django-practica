from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Primer mensaje")
# Create your views here.
