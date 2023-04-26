from django.shortcuts import render

# Create your views here.
def home(request):
    d={'name':'timoothy','age':'27'}
    return render(request,'index.html',d)