from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def relationship(request):
    return render(request, 'relationship.html')

def composition(request):
    return render(request, 'composition.html')

def distribution(request):
    return render(request, 'distribution.html')

def comparison(request):
    return render(request, 'comparison.html')
