from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':" is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is the Service page $")

def contact(request):
    return HttpResponse("This is the contact page")
