from django.shortcuts import render, redirect
from django.contrib import  messages
# from django.contrib.auth import authenticate, login, logout?
from django.contrib.auth import authenticate , login, logout
from registerapp import models
from registerapp import forms
# Create your views here.

def index(req):
    form = forms.RegisterPageForm()
    if req.method == 'POST':
        form = forms.RegisterPageForm(req.POST)
        if form.is_vlaid():
            if password == confirmPassword:
                User.objects.create_user(username=username, password=password, email=email)
                form.save()
                messages.add_message(request,messages.SUCCESS ,"Your success")
            else:
                messages.add_message(request, messages.WARNING , "Password doesn't match.")
            form.save()
            redirect('login')
    context = {
        'form': form
    }
    return render(req, 'index.html', context)
    

def register(req):
    form = forms.RegisterPageForm()
    if req.method == 'POST':
        form = forms.RegisterPageForm(req.POST)
        print('step1')
        if form.is_valid():
            form.save()
            return redirect('login1')
            messages.add_message(request,messages.SUCCESS ,"Your success")
    context = {
        'form': form
    }
    return render(req, 'register.html', context)

def login1(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        user = authenticate(request, email =  email, password = password)
        print("User", user)
        if user is not None:
            print(user)
            login(request,user)
            return redirect('index')
        else :
            return redirect('login1')

    return render(request, 'login.html')   
