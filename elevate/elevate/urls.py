from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

def register(request):
    return HttpResponse("이건 등록 페이지")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',register)
]
