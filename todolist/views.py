import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from todolist.models import Task
from todolist.forms import CreateNewTask

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    form = CreateNewTask()
    user = request.user
    context = {
        "username": user.username,
        "form": form
    }
    return render(request, "todolist.html", context)

def show_todolist_json(request):
    user = request.user
    todolist_item = Task.objects.filter(user=user)
    return HttpResponse(serializers.serialize('json', todolist_item), content_type="application/json")

@login_required(login_url="login/")
@csrf_exempt
def add_task_ajax(request):
    form = CreateNewTask()

    if request.method == "POST":
        form = CreateNewTask(request.POST)

        if form.is_valid():
            user = request.user
            data = form.cleaned_data
            task = Task.objects.create(**data, user=user)
            result = {
                "fields": {
                    "title": task.title,
                    "description": task.description,
                    "is_finished": task.is_finished,
                    "date": task.date,
                },
                "pk": task.pk,
                "status": "created",
            }

        return JsonResponse(result)

@login_required(login_url="/todolist/login/")
def create_task(request):
    
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        
        new_task = Task(title=title, description=description)
        new_task.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@login_required(login_url="/todolist/login/")
@csrf_exempt
def delete_task(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return JsonResponse({"status": "deleted"})

@login_required(login_url="/todolist/login/")
@csrf_exempt
def update_task(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, id=pk)
        is_finished = not task.is_finished
        task.is_finished = is_finished
        task.save()
        return JsonResponse({"is_finished": is_finished, "status": "updated"})

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
    return redirect('todolist:login')

