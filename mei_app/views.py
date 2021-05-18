

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("---placeholder to later display a list of all blogs")

def create(request):
    return redirect('/')

def show(request, id):
    return HttpResponse(f"placeholder to display blog number:{id}") #debug not showing actual number

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number): 
    return redirect('/')
