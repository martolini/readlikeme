from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from readlikeme.external.django_ajax.decorators import ajax
from .models import ViewCount
from readlikeme.app.reader.models import Article


@ajax
@login_required
def view_count(request):
	if request.POST:
		article = Article.objects.get(id=request.POST.get('a_id'))
		filtered_views = article.viewcount.filter(user=request.user)
		if len(filtered_views) == 0:
			ViewCount(user=request.user, content_object=article).save()
		return {'inner-fragments': {'#article-%d-views' % article.id: article.viewcount.count()}}