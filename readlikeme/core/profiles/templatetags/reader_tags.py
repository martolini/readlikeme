from django import template
from readlikeme.core.profiles.models import Reader
from django.db.models import Q
register = template.Library()

@register.inclusion_tag('reader_dashboard.jade', takes_context = True)
def show_reader_dashboard(context):
	reader = context['user']
	readers = Reader.objects.exclude(pk=reader.pk).exclude(id__in=reader.following.all())
	return {'user': context['user'], 'suggested_readers': readers}

@register.inclusion_tag('list_readers.jade', takes_context = True)
def list_readers(context, readers):
	return {'user': context['user'], 'readers': readers}