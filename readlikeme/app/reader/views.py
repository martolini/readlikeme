from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from readlikeme.core.profiles.models import Reader
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from random import randint

def frontpage(request):
	if request.user.is_authenticated():
		articles = Article.objects.filter(author__in=request.user.following.all).order_by('-posted_at') | Article.objects.filter(author=request.user).order_by('-posted_at')
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

def search_view(request):
	if request.POST:
		query = request.POST.get('query')
		articles_on_url = Article.objects.filter(url__icontains=query)
		articles_on_title = Article.objects.filter(title__icontains=query)
		articles_on_description = Article.objects.filter(description__icontains=query)
		articles = articles_on_url | articles_on_title | articles_on_description
		readers = Reader.objects.filter(username__icontains=query).exclude(username=request.user.username)
		return render(request, 'search.jade', {'articles': articles, 'readers': readers})
	return render(request, 'search.jade', {'articles': Article.objects.all(), 'readers': Reader.objects.all()})
