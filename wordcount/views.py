from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere': 'This is me'})

def eggs(request):
    return HttpResponse('eggs')

def count(request):
    name = request.GET['name']
    wordlist = name.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            #increase
            worddict[word] += 1
        else:
            #add to the dict
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'name': name, 'count': len(wordlist), 'sortedwords': sortedwords})
