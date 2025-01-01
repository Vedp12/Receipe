from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

#? This is default webpage  
def default(request):
    return HttpResponse("Hello")

def receipe(request):
    
    if request.method=="POST":
        Name=request.POST.get("Name")
        Description=request.POST.get("Description")
        Ingredients=request.POST.get("Ingredients")
        Iamge=request.FILES.get("Iamge")
        
        print(Name, Description, Ingredients, Iamge)
        # print(f"{}")
        
        Receipe.objects.create(
            Name=Name, 
            Description=Description,
            Ingredients=Ingredients,
            Iamge=Iamge
            )
        return redirect('/Receipe/')
    # query_set=Receipe.objects.all()
    return render(request,"Receipe.html",{'Receipe':Receipe.objects.all()})

def Deletereceipe(request ,id):
    print(f"This is Receipe's id = {id}")
    query_set = Receipe.objects.get(id=id)
    query_set.delete()
    return redirect('/Receipe/')