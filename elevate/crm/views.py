from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    
    clientList = [
        {
            'id':'1',
            'name' : 'John Doe',
            'occupation' : 'Electrical engineer'
        },
        {
            'id':'2',
            'name' : 'Kate Smith',
            'occupation' : 'Lawyer'
        },
    ]
    
    context ={
        'mainClientList' : clientList
    }
    
    
    return render(request,"crm/index.html",context)

def register(request):
    return render(request,'crm/register.html')