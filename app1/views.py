from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'app1/home.html')

def password(request):

    characters= list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))

    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))


    len= int(request.GET.get("length",12))

    pwd=''

    for i in range(len):
        pwd+= random.choice(characters)
    return render(request,'app1/password.html',{'password' : pwd})

def about(request):
    return render(request,'app1/about.html')

