from django.contrib import admin

from .models import Article, Tags, TagConnector

class TagConnectorInline(admin.TabularInline):
    model = TagConnector
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagConnectorInline]
    pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    inlines = [TagConnectorInline]
    pass


@admin.register(TagConnector)
class TagConnector(admin.ModelAdmin):
    pass
