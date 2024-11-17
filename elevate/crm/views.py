from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from .forms import TaskForm
# Create your views here.
def homepage(request):
    return render(request,"crm/index.html")

def task(request):
    
    queryDataSingle = Task.objects.get(id=3)
    
    context = {'task':queryDataSingle}
    
    return render(request, 'crm/task.html',context)

def register(request):
    return render(request,'crm/register.html')

def task_form(request):
    form = TaskForm()
    
    context = {"TaskForm":form}
    return render(request,'crm/task-form.html',context)