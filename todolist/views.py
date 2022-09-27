import datetime
from multiprocessing import context
from tkinter import E
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from todolist.models import Task
from todolist.forms import CreateNewTask

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    data_todolist = Task.objects.filter(user= user)
    context = {
        "username": user.username,
        'todolist': data_todolist,
        'last_login': request.COOKIES['last_login'],
    }
    
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/todolist/login/")
def create_task(request):
    
    if request.method == "POST":
        form = CreateNewTask(request.POST)
        
        if form.is_valid():
            user = request.user
            data = form.cleaned_data
            print(data)
            Task.objects.create(user=user, **data)
            return HttpResponseRedirect(reverse("todolist:show_todolist"))
        
    else:
        form = CreateNewTask()
        
    context = {
        "form": form
    }

    return render(request, 'create-task.html', context)

def delete_task(request, pk):
    # user = request.user
    deleted_task = Task.objects.get(pk = pk)
    deleted_task.delete()
    return redirect("todolist:show_todolist")

def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_finished = not task.is_finished
    task.save()
    return redirect("todolist:show_todolist")
    
    