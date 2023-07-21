from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def third(request):
    return HttpResponse('<h1>THIS IS MY THIRD REPOSITORY</h1>')
def fourth(request):
    return HttpResponse('<h1>THIS IS MY FOURTH REPOSITORY</h1>')
