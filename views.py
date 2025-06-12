from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login 
# Create your views here.

def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        data = User.objects.create_user(username=username, email=email, password=password)
        data.save()
        
        return redirect('login')

    return render(request, "signup.html")


def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else :
            return render(request, 'login.html', {"error": 'Invalid credentials'})

    return render(request, 'login.html')
