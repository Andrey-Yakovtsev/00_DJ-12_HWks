from django.template import library

register = library.Library()


@register.filter()
def sort(tagslist):
    pass
