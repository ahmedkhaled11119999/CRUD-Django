from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
from user.models import MyUser
from student.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin
from django.urls import reverse


def home(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'user/home.html', context)


def login(request):
    if request.method == 'GET':
        return render(request, "user/login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = MyUser.objects.get(email=email, password=password)
            admin_user = authenticate(username=user.username, password=password)
            if user and admin_user is not None:
                request.session['username'] = user.username
                authlogin(request, admin_user)
                return redirect('home')
        except MyUser.DoesNotExist:
            error_msg = "Your credentials is not correct"
            context = {'error': error_msg}
            return redirect("/login/", context)



def register(request):
    if request.method == 'GET':
        return render(request, "user/register.html")
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        MyUser.objects.create(username=username, email=email, password=password)
        User.objects.create_user(username, email, password, is_staff=True)
        return redirect("login")
    else:
        return HttpResponse("Unsupported request method")


def logout(request):
    request.session.clear()
    return redirect("login")


