from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return HttpResponse("this is a placeholder")
# Create your views here.

def new(request):
    return HttpResponse("another general thing")

def create(request):
    return redirect("/")

def number(request, number):
    number = str(number)
    return HttpResponse("wassup I'm the number " + number)

def edit(request, number):
    number = str(number)
    return HttpResponse("we gonna edit " + number)

def destroy(request, number):
    number = str(number)
    return HttpResponse("buh-bye " + number)