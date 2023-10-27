from django.shortcuts import render,HttpResponse

# Create your views here.
def gateway(request):
    return HttpResponse("<h1>Payment </h1>")

def succesfull(request):
    return HttpResponse("<h1>payment is succesfull</h1>")

def unsuccesfull(request):
    return HttpResponse("<h1>payment is unsuccesful</h1>")