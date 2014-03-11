from readlikeme.external.django_ajax.decorators import ajax
from .models import Reader
from django.shortcuts import get_object_or_404, redirect

@ajax
def follow_reader(request):
	if request.POST:
		follower_id = request.POST.get('follower_id')
		follower = get_object_or_404(Reader, id=follower_id)
		reader = request.user
		data = {'inner-fragments': {}}
		if follower in reader.following.all():
			reader.following.remove(follower)
			data['inner-fragments']['#follow_%s' % follower_id] = 'Follow'
		else:
			reader.following.add(follower)
			data['inner-fragments']['#follow_%s' % follower_id] = 'Unfollow'
		reader.save()
		data['inner-fragments']['#user-following-count'] = reader.following.count()
		return data