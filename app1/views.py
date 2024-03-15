from django.shortcuts import render

# Create your views here.
def index (request):
    return render (request,'main.html')
def secondPage (request):
    return render (request,'second.html')