from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render( request , 'home.html')

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()

    wordic = {}

    for word in wordlist:
        if word in wordic:
            wordic[word] += 1
        else:
            wordic[word] = 1

    print(wordic)

    return render(request, 'count.html', {"fulltext": fulltext, "count": len(wordlist), "wordic1": wordic.items() } )

def about(request):

    return render(request , "about.html")
