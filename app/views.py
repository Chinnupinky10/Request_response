from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def janu(request):
    return HttpResponse('<h1><marquee>hai raj how are u</h1></marquee>')

def raj(request):
    return HttpResponse('<h1><marquee>hai  janu how are u</h1></marquee>')
