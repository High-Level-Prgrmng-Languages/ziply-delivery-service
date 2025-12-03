from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as Login
# Create your views here.


def package(request):
    return render(request, 'package.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            Login(request, user)
            return redirect('packages')  # Redirect after successful login
        else:
            return render(request, 'login.html')
