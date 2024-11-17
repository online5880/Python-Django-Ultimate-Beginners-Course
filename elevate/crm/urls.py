from django.urls import path
from . import views


urlpatterns = [
    path("",views.homepage,name=""),
    path('create-task',views.create_task,name='create-task'),
    path('view-tasks',views.tasks,name='view-tasks'),
    path("register",views.register,name="register"),
]
