#I have created this file on my own
from ssl import Purpose
from django.http import HttpResponse #imported for httpresponse
from django.shortcuts import render

#Code for Video:6
# def index(request):
#     return HttpResponse('''
#     <h2>Navigation Bar </h2>
#       <a href= "https://www.youtube.com/" > Youtube</a><br>
#     <a href="https://www.facebook.com/"> Facebook </a> <br>
#     <a href="https://www.flipkart.com/"> Flipkart </a> <br>
#     <a href="https://www.hindustantimes.com/"> News </a> <br>
#     <a href="https://www.google.com/"> Google </a> <br>
#     ''')

# def about(request):
#     return HttpResponse("Pre-final Year Student at Thapar University,Patiala")


#code for video:7
def index(request):
   return render(request,'index.html')

def analyze(request):
    #get the text and remove punc filter state
    djtext= request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','default')
    # print(removepunc)
    # print(djtext)
    #analyse the text
    if removepunc == "on":
     punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     analyzed=""

     for ele in djtext:
      if ele not in punc:
        analyzed=analyzed + ele

     params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
     return render(request,'analyse.html',params)

    else:
        return HttpResponse("ERROR")

# def removepunc(request):
#     return HttpResponse("Removed Punctuations")


