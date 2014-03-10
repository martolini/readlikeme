from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import User
from .forms import UserCreateForm, AuthenticateForm

def login_view(request):
	if request.POST:
		form = AuthenticateForm(data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			return redirect('/')
	return redirect('/')

def logout_view(request):
	logout(request)
	return redirect('/')

def signup_view(request):
	if request.POST:
		form = UserCreateForm(request.POST)
		if form.is_valid():
			username = form.clean_username()
			password = form.clean_password2()
			form.save()
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/')
	return redirect('/')