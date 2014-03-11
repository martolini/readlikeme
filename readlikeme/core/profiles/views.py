from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import Reader
from .forms import ReaderCreationForm, AuthenticateForm, ReaderChangeForm
from django.core.urlresolvers import reverse


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
			return redirect(reverse('profile', args=(reader.username, )))
	return redirect('/')

def profile_view(request, username=False):
	reader = get_object_or_404(Reader, username=username)
	form = ReaderChangeForm(instance=reader)
	return render(request, 'profile.jade', {'reader': reader, 'form': form})

def edit_profile(request):
	if request.POST:
		form = ReaderChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
		else:
			print form.errors
	return redirect(reverse('profile', args=(request.user.username, )))