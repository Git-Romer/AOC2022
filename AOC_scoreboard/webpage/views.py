from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def bongocat(request):
    return render(request, 'bongo_cat.html', {})