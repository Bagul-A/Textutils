#my site
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    caps=request.GET.get('capitalise','off')
    ccount=request.GET.get('charcount','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzedtext': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if caps == "on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzedtext': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if ccount == "on":
        analyzed=len(djtext)
        params = {'purpose': 'UPPERCASE', 'analyzedtext': analyzed}
        djtext=analyzed
       #  return render(request, 'analyze.html', params)
    if removepunc != "on" and caps != "on" and ccount != "on":
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)