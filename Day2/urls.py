"""Day2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import *
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('delete-student/<id>/', delete_student, name="delete_student"),
    path('create-student/', create_student, name='create_student'),
    path('update-student/<id>/', update_student, name='update_student'),
    path('select-student/', select_student, name='select_student'),
    path('logout/', logout, name='logout')

]
