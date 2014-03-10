from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from readlikeme.core.profiles.models import User
from readlikeme.core.profiles.forms import UserCreateForm, AuthenticateForm
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required



def frontpage(request):
	articles = Article.objects.filter(author__in=request.user.followees.all) | Article.objects.filter(author=request.user)
	return render(request, 'frontpage.jade', {'articles': articles})


@login_required
def post_article(request):
	if request.POST:
		url = request.POST.get('url')
		article = Article(url=url, author=request.user)
		article.save()
		return redirect('/')
	return redirect('/')
