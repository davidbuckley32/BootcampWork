from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    response = create('')
    return response

def show(request, number):
    number = str(number)
    return HttpResponse("placeholder to display blog number " + number)

def edit(request, number):
    number = str(number)
    return HttpResponse("placeholder to edit blog number " + number)
# Create your views here.
