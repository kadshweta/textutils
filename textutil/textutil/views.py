# code for v-6

from django.http import HttpResponse
from django.shortcuts import render 
# def index(request):
#     return HttpResponse('''<h1>hello shweta</h1> 
#                         <a href="https://www.youtube.com/ "> you tube </a> ''')


# special for pipline code 

def index(request):
    # return HttpResponse("<h1> Home </h1> ")
    # params={'name':'shweta','place':'mankhurd'}
    return render(request,'index.html')

#---------------------------Remove punctuation ---------------

def analyze(request):
    # Get the text
    djtext= request.POST.get('text', 'default')
    print(djtext) 

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline_rm=request.POST.get('newline_rm','off')
    space_rm=request.POST.get('space_rm','off')
    extraspace_rm=request.POST.get('extraspace_rm','off')


    # print(removepunc)
    print(djtext) 
    # analyzed=djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # Analyze text
        djtext=analyzed
        # return render(request, 'analyze.html', params)
        # done with remove punctuation !@#$%^

    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Full capital Charcters', 'analyzed_text': analyzed}
        # Analyze text
        djtext=analyzed

        # return render(request, 'analyze.html', params)
    
    if (newline_rm=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed +char
        params = {'purpose': 'New line Charcters', 'analyzed_text': analyzed}
        # Analyze text
        djtext=analyzed

        # return render(request, 'analyze.html', params)

    if (space_rm=="on"):
        analyzed=""
        space =" "
        for char in djtext:
            if char!=space:
                analyzed=analyzed+char
        params = {'purpose': 'space Remover', 'analyzed_text': analyzed}
        # Analyze text
        djtext=analyzed

        # return render(request, 'analyze.html', params)
    
    if (extraspace_rm=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if  not(djtext[index] == " " and djtext[index+1]==" "):
               analyzed+=char
        params = {'purpose': 'space Remover', 'analyzed_text': analyzed}
        # Analyze text
        djtext=analyzed
        
    if(removepunc != "on" and fullcaps!="on" and extraspace_rm!="on" and space_rm!="on" and newline_rm !="on"):
        return HttpResponse("please select any operation and try again")
        
    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")
            
    


# def capfirst(request):
#     return HttpResponse("capitalize")

# def spacerem(request):
#     return HttpResponse("space remover")