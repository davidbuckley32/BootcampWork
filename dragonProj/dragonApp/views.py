from django.shortcuts import render, HttpResponse, redirect

#/
def index(request):
    return HttpResponse("Here there be dragons!")

#/dragons (show dragons here)
def show_dragons(request):
    context = {
        "all_dragons":request.POST['dragon_name']
    }
    return render(request, "show_dragons.html", context)
    # return render(request, "show_dragons.html")
    # return HttpResponse("This is a list of all dragons.")

#/dragons/new (Submit FORM HERE) HOLDS form
def new_dragons(request):
    return render(request, "new_dragons.html")

#/dragons/create (Create Dragons here)
def create_dragons(request):
    if request.method == "POST":
        print("Dragon Created!")
        return redirect("/dragons")
    return redirect("/dragons/new")

#/dragons/<dragon_id>/edit
def edit_dragons(request, dragon_id):
    context = {
        "dragon_id":dragon_id,
        "dragon_colors":['black', 'red', 'blue', 'green', 'white']
    }
    return render(request, "edit.html", context)
    # return HttpResponse(f"Edit Dragon with id {dragon_id}") #why do you need the f
