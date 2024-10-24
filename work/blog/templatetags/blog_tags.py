from ..models import BlogCategory, Tag
from django.template import Library, loader

register = Library()


@register.inclusion_tag('categories_list.html',
                        takes_context=True)
def categories_list(context):
    categories = BlogCategory.objects.all()
    return {
        'request': context['request'],
        'categories': categories
    }

@register.inclusion_tag('tags_list.html',
                        takes_context=True)
def tags_list(context):
    tags = Tag.objects.all()
    return {
        'request': context['request'],
        'tags': tags
    }