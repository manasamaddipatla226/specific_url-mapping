from django.shortcuts import render
from django.http import HttpResponse
def smart_work(request):
    return HttpResponse('<h1><marquee> smart work is better than hard work </marquee></h1>')
def friend(request):
    return HttpResponse('<h1> A friend in need is a friend in deed </h>')
# Create your views here.
