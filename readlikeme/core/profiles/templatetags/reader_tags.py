from django import template

register = template.Library()

@register.inclusion_tag('reader_dashboard.jade', takes_context = True)
def show_reader_dashboard(context):
	return {'user': context['user']}

@register.inclusion_tag('list_readers.jade', takes_context = True)
def list_readers(context, readers):
	return {'user': context['user'], 'readers': readers}