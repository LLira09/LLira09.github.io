from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

def writenow(request):
    return render(request, 'portfolio/writenow.html')

def graphic(request):
    return render(request, 'portfolio/graphicdesign.html')

def newjersey(request):
    return render(request, 'portfolio/newjersey.html')
