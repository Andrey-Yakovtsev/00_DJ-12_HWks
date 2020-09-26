from django.contrib import admin

from .models import Article, Tags

# class Tagmembership(admin.TabularInline):
#     model = Article.title.through
#     pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # inlines = [
    #     Tagmembership
    # ]
    pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    # inlines = [
    #     Tagmembership
    # ]
    pass


