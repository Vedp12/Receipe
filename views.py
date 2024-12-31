from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

#? This is default webpage  
def default(request):
    return HttpResponse("Hello")

def receipe1(request):
    
    if request.method=="POST":
        Name=request.POST.get("Name")
        Description=request.POST.get("Description")
        Ingredients=request.POST.get("Ingredients")
        Image=request.FILES.get("Iamge")
        
        print(Name, Description, Ingredients)
        print(f"{Image}")
        
        Receipe.objects.create(
            Name=Name, 
            Description=Description,
            Ingredients=Ingredients,
            Iamge=Image
        )
        
    return render(request,"Receipe.html")
