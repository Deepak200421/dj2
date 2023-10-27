from django.shortcuts import render,HttpResponse

# Create your views here.
def feedback(request):
    return HttpResponse("<h1>give me feedback </h1>")

def rating(request):
    return HttpResponse("<h1>give me rating</h1>")

def star(request):
    return HttpResponse("<h1>give me rating as stars</h1>")
