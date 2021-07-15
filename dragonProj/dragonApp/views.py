from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("Here there be dragons!")

def show_dragons(request):
    return render(request, "index.html")
    # return HttpResponse("This is a list of all dragons.")

def edit_dragon(request, dragon_id):
    context = {
        "dragon_id":dragon_id,
    }
    return render(request, "edit.html", context)
    # return HttpResponse(f"Edit Dragon with id {dragon_id}") #why do you need the f

def create_dragons(request):
    #this is where we create a dragon
    return redirect("/dragons")