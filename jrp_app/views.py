from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'index.html')

def singup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password!=cpassword:
            return HttpResponse('your password does not match')
        
        else:
            user = User.objects.create_user(username, email, address, password)
            user.save()
            return redirect('login')

    return render(request, 'singup.html')

def Login(request):
    if request.method=="POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("invalid login details")

    return render(request, 'Login.html')

def home(request):
    return render(request, 'index.html')

def Logout(request):
    logout(request)
    return redirect('login')

def card(request):
    return render(request, 'card.html')

def doctor(request):
    return render(request, 'doctor.html')