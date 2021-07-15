from django.shortcuts import render
from django.utils.crypto import get_random_string

def index(request):
    pass

def random(request):
    return render(request, "random.html")