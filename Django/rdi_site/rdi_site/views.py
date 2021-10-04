from django.http import HttpResponse


def hola(request):
    return HttpResponse("Hola Dejango!! Hello, world. You're at the polls index.")