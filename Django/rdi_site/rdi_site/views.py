# from django.http import HttpResponse
from django.shortcuts import render


def hola(request):
    return render(request, 'home.html')
