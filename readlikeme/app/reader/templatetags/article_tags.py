from django import template

register = template.Library()

@register.inclusion_tag('list_articles.jade', takes_context = True)
def list_articles(context, articles):
	return {'user': context['user'], 'articles': articles}