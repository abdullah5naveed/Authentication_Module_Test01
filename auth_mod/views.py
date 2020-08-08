from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'auth_mod/home.html')



def signupuser(request):
    creationform = UserCreationForm
    SignupData = {'signupform':creationform}
    return render(request, 'auth_mod/signup.html', SignupData)



def loginuser(request):
    return render(request, 'auth_mod/login.html')

