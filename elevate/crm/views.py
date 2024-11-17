from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm, CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def homepage(request):
    return render(request,"crm/index.html")

# CRUD - Create
def create_task(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-tasks')
    
    context = {"TaskForm":form}
    return render(request,'crm/create-task.html',context)

# CRUD - Read
def tasks(request):
    
    queryDataAll = Task.objects.all()
    
    context = {'AllTasks':queryDataAll}
    
    return render(request, 'crm/view-tasks.html',context)


# CRUD - Update
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            return redirect('view-tasks')
        
    context = {'UpdateTask' : form}
    return render(request, 'crm/update-task.html',context)

# CRUD - DELETE
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('view-tasks')
    
    return render(request, 'crm/delete-task.html')

# Registration webpage
def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User created")
        
    context = {'RegistrationForm' : form}
    
    return render(request,'crm/register.html',context)


# Login
def my_login(request):
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password = password)
            
            if user is not None:
                login(request, user)
                
                return redirect('dashboard')
            
    context = {'LoginForm':form}
    return render(request,'crm/my-login.html',context)
            

# Dashboard
def dashboard(request):
    return render(request, 'crm/dashboard.html')
