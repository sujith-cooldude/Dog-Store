from django.shortcuts import render
import json

dogData = open(r"F:\learnings\Django_tuts\dogstore\dogs.json","r")
data = json.load(dogData)
# Create your views here.
def index(request):
    context = {
        "dogs":data
    }
    return render(request,"dogs/index.html",context)

def show(request,id):
    for dog in data:
        if dog["id"] == id:
            singleDog = {"dog":dog}
    return render(request,"dogs/show.html",singleDog)