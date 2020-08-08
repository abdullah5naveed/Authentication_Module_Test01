from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'auth_mod/home.html')



def signupuser(request):
    if request.method == 'GET':
        signupData =  {'signupform':UserCreationForm}
        return render(request, 'auth_mod/signup.html', signupData)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')

            except IntegrityError:
                signupData =  {'signupform':UserCreationForm, 'error': "User Name Must be unique."}
                return render(request, 'auth_mod/signup.html', signupData)
        else:
            signupData =  {'signupform':UserCreationForm, 'error': "Password didn't match"}
            return render(request, 'auth_mod/signup.html', signupData)
    

def loginuser(request):
    return render(request, 'auth_mod/login.html')




def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'auth_mod/home.html')