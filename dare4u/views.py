from django.shortcuts import render

# Create your views here.



def start(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def privacy(request):
    return render(request,'privacy.html')

def disclaimer(request):
    return render(request,'disclaimer.html')

def tfquiz(request):
    return render(request,'tfquiz.html')

def ynquiz(request):
    return render(request,'tfquiz.html')

def quiz(request):
    return render(request,'quiz.html')

def tquiz(request):
    return render(request,'19quiz.html')

def ynnquiz(request):
    return render(request,'ynnquiz.html')

