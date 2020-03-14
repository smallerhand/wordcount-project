from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'hithere': 'This is me'})

def eggs(request):
    return HttpResponse('eggs')

def count(request):
    name = request.GET['name']
    wordlist = name.split()
    return render(request, 'count.html', {'name': name, 'count': len(wordlist)})
