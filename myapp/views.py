from django.shortcuts import render

# Create your views here.
def myfun(request):
    return render(request,'index.html')
def myfun1(request):
    return render(request,'register.html')