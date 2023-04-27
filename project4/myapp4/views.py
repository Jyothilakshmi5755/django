from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')
def home2(request):
   return render(request,'index.html')
def home3(request):
   return render(request,'about.html')
