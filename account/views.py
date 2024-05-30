from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm

def index(request):
    return render(request, 'account/home.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = SignupForm()
    return render(request,"account/signup.html",{"form":form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('account:home')
    else:
        form = LoginForm()
    return render(request,'account/login.html',{"form":form})

def user_logout(request):
    logout(request)
    return redirect("account:login")