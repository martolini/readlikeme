from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from readlikeme.core.profiles.models import Reader
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse


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

def purchase_credits(request):
	paypal_dict = {
	"business": settings.PAYPAL_RECEIVER_EMAIL,
	"amount": "1.00",
	"item_name": "1000 Credits",
	"invoice": "23987",
	"notify_url": "http://www.readlike.me" + reverse('paypal-ipn'),
	"return_url": "http://www.readlike.me/credits/return/",
	"cancel_return": "http://www.readlike.me/credits/cancel/",
	}
	form = PayPalPaymentsForm(initial=paypal_dict)
	return render(request, "purchase.jade", {'form': form})

@csrf_exempt
def purchase_return(request):
	if request.POST:
		print 'post: ',
		print request.POST
	return render(request, 'purchase_return.jade')
@csrf_exempt
def purchase_cancel(request):
	if request.POST:
		print 'post: ', 
		print request.POST
	return render(request, 'purschase_cancel.jade')
