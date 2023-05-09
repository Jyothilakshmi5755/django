from django.shortcuts import render
from app5.models import student
from app5.models import B
from app5.forms import studentForm

# Create your views here.
def list(request):
    k=student.objects.all()
    return render(request,'list.html',{"s":k})
# def list(request):
#     k=B.objects.all()
#     return render(request,'list.html',{"s":k})

def form1(request):
    form=studentForm()
    if request.method=='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
            return list(request)
        else:
            form=studentForm()
    return render(request,'form.html',{"form":form})
