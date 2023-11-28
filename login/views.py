from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm

def login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)                             #(1)
        if form.is_valid():                                        #(2)
            request.session['user'] = form.user_id                 #(3)
            return redirect('/')
    else:
        form = LoginForm()                                         #(4)
    
    return render(request, 'login.html', { 'form':form }) 

