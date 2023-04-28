from django.shortcuts import render
from app5.models import student

# Create your views here.
def list(request):
    k=student.objects.all()
    return render(request,'list.html',{"s":k})
