from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from readlikeme.core.profiles.models import User
from readlikeme.core.profiles.forms import UserCreateForm, AuthenticateForm
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required



def frontpage(request):
	if request.user.is_authenticated():
		articles = Article.objects.filter(author__in=request.user.followees.all).order_by('-posted_at') | Article.objects.filter(author=request.user).order_by('-posted_at')
	else:
		articles = Article.objects.order_by('-posted_at')[:10]
	return render(request, 'frontpage.jade', {'articles': articles})


@login_required
def post_article(request):
	if request.POST:
		url = request.POST.get('url')
		article = Article(url=url, author=request.user)
		article.save()
		return redirect('/')
	return redirect('/')
