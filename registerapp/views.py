from django.shortcuts import render, redirect
from django.contrib import  messages
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required

from registerapp import models
from registerapp import forms
# Create your views here.

def index(req):
    return render(req, 'index.html')

@login_required
def viewpage(req):
    obj = models.RegisterPage.objects.all()
    context = {
        'data': obj
    }
    return render(req, 'viewpage.html', context)
    

def register(req):
    form = forms.RegisterPageForm()
    if req.method == 'POST':
        form = forms.RegisterPageForm(req.POST)
        print('step1')
        if form.is_valid():
            form.save()
            messages.add_message(req,messages.SUCCESS ,"Register successfull")
            return redirect('register')
    context = {
        'form': form
    }
    return render(req, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login_view')

def login_view(request):
    form = forms.AuthenticationForm()
    user = request.user
    if user.is_authenticated:
        return redirect('viewpage')
    if request.POST:
        form = forms.AuthenticationForm(request.POST) 
        if form.is_valid():
            email = request.POST['email']
            password= request.POST['password']
            user = authenticate(email =  email, password = password)
            if user:
                login(request, user)
                return redirect('viewpage')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)
