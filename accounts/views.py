import email
import re
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
import logging
logger = logging.getLogger(__name__)


# Create your views here.

def loginreq(request):
    context = {}
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pass']            
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context['error'] = "Invalid username or password."
            return render(request, 'auth/login.html', context)
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        # Check if user exists
        username = request.POST['uname']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email,
                                            password=password)
            login(request, user)
            return redirect('/')
        else:
            context = {}
            context['error'] = "User already exists."
            return render(request, 'auth/register.html', context)

def logout_req(request):
    logout(request)
    return render(request, 'home.html')