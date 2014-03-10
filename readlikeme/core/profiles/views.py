from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import Reader
from .forms import ReaderCreationForm, AuthenticateForm, ReaderChangeForm

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
		form = ReaderCreationForm(request.POST)
		if form.is_valid():
			username = form.clean_username()
			password = form.clean_password2()
			form.save()
			reader = authenticate(username=username, password=password)
			login(request, reader)
			return redirect('/')
	return redirect('/')

def profile_view(request, username=False):
	reader = get_object_or_404(Reader, username=username)
	return render(request, 'profile.jade', {'reader': reader})

def edit_profile(request):
	if request.POST:
		form = ReaderChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			reader = request.user
			reader.first_name = form.cleaned_data['first_name'] or reader.first_name
			reader.last_name = form.cleaned_data['last_name'] or reader.last_name
			if request.POST.get('password'):
				reader.set_password(request.POST.get('password'))
				#reader.set_password(form.cleaned_data['password'])
			reader.save()
		else:
			print form.errors
	return redirect('/reader/martin')
