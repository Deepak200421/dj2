from django.shortcuts import render,HttpResponse

# Create your views here.
def gallery(request):
    return HttpResponse("<h1>View  Arts Gallery Here</h1>")

def offer(request):
    return HttpResponse("<h1>Latest offers are</h1>")

def contact(request):
    return HttpResponse("<h1>If there is any issue contact us</h1>")
