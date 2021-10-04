from django.shortcuts import render
# from django.http import HttpResponse
from .models import Course

# Create your views here.


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
