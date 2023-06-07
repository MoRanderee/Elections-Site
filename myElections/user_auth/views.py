from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout

from .forms import SignUpForm

# Create your views here.

"""
this method redirects the user to the login page
"""
def user_login(request):
    return render(request, 'authentication/login.html')

"""
this method checks if the user exists in the DB
"""
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    # if the user is not found, refresh the login page using the 'login' view
    if user is None:
        messages.error(request, "Unsuccessful login. Invalid information.")
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )

    # if the user is found, redirect them to the polls home page using the 'index' view     
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('polls:poll') # the poll view in the polls app
        )

"""
this method provides the user with the ability to sign up and add their details to the DB
"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('user_auth:login') # the poll view in the polls app
        
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    
    form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})

"""
this method allows the user to logout of their profile
"""
def logout_view(request):
    logout(request)