from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Tags, TagConnector


def articles_list(request):
    template = 'articles/news.html'
    # articles_data = Article.objects.prefetch_related('tagconnector_set')
    #
    # context = {'object_list': articles_data
    # }

    context = {'object_list': Article.objects.order_by('published_at'),
               'tags': Tags.objects.all(),
               'tagconnectors': TagConnector.objects.all()
               }

    return render(request, template, context)
