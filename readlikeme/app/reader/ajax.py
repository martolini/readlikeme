from readlikeme.external.django_ajax.decorators import ajax
from .models import Article
from django.shortcuts import get_object_or_404, redirect

@ajax
def delete_article(request):
	if request.POST:
		article_id = request.POST.get('article_id')
		article = get_object_or_404(Article, id=article_id)
		article.delete()
		return {'status': 'OK'}