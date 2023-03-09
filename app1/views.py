from django.shortcuts import render
from django.http import HttpResponse
def practice(request):
    return HttpResponse('<h1> practice makes man perfect </h1>')
def end(request):
    return HttpResponse('<h1> every end leads with a new beginning </h1>')

# Create your views here.
