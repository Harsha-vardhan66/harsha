from django.http import HttpResponse
from django.shortcuts import render
def ram(request):
    return HttpResponse("Haii Harsha")
def wel(request):
    return HttpResponse("<h1>Welcome To My Block<h1>")
def ramu(request):
    return render(request,"ram2.html",{"vlr":"123456789"})
def ram1(request):
    return render(request,"countwords.html")
def count(request):
    mess=request.GET['message']
    w1=mess.split()
    return render(request,"count.html",{"msg":mess,"length":len(w1)})
def aboutus(request):
    return render(request,"aboutus.html")