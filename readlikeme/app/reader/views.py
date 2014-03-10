from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from readlikeme.core.profiles.models import User
from readlikeme.core.profiles.forms import UserCreateForm, AuthenticateForm
from .forms import ArticleForm
from .models import Article


def frontpage(request, auth_form=None, user_form=None):
	return render(request, 'frontpage.jade')
