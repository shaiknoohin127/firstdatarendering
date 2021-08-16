from django.shortcuts import render

# Create your views here.
def datarender(request):
    return render(request,'renderdata.html',context={'name':'shaik Noohin'})