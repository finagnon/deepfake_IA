from django.shortcuts import render
from django.http import HttpResponse


def fonct(request):
    return render(request, 'index.html')