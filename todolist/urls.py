from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='todolist'),
    path("update-task/<int:pk>/", update_task, name="update-task"),
    path("delete-task/<int:pk>/", delete_task, name="delete-task"),
]