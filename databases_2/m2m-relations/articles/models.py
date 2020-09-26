from django.db import models




class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tags(models.Model):

    article_name = models.ManyToManyField(Article, related_name='tag', through='Tagmembership')
    tag_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Наименование тэга')
    is_main = models.BooleanField(blank=True, default='')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэгз'

    def __str__(self):
        return self.tag_name


class Tagmembership(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
