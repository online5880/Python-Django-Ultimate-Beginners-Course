from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {
        "first_name":"Kate Johnson"
    }
    return render(request,"crm/index.html",context)

def register(request):
    return render(request,'crm/register.html')