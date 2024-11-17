from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",views.homepage,name=""),
    path('create-task',views.create_task,name='create-task'),
    path('view-tasks',views.tasks,name='view-tasks'),
    path('update-task/<str:pk>',views.update_task,name='update-task'),
    path('delete-task/<str:pk>',views.delete_task,name='delete-task'),
    path("register",views.register,name="register"),
    
    path("my-login",views.my_login, name="my-login"),
    path("user-logout",LogoutView.as_view(),name='user-logout'),
    path("dashboard",views.dashboard,name="dashboard"),
]
