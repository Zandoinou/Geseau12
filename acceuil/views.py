from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'acceuil/index.html')

def connexion(request):
    return render(request,'acceuil/login.html')

def register(request):
    return render(request,'acceuil/register.html')