from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseBadRequest
from user.models import MyUser


def home(request):
    return render(request, "user/home.html")


def login(request):
    if request.method == 'GET':
        return render(request, "user/login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_user_exist = MyUser.objects.all().filter(email=email, password=password)
        if is_user_exist:
            context = {'username': is_user_exist[0].username}
            return render(request, 'user/home.html', context)
        else:
            return HttpResponseBadRequest("Sorry, your credentials is in correct")


def register(request):
    if request.method == 'GET':
        return render(request, "user/register.html")
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        MyUser.objects.create(username=username, email=email, password=password)
        return redirect("login")
    else:
        return HttpResponse("Unsupported request method")