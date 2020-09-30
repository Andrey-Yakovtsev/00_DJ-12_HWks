from django.contrib import admin


from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Car, Review


class ReviewAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = Review
        fields = '__all__'


class CarAdmin(admin.ModelAdmin):

    list_display = ('brand', 'model', 'review_count')
    list_filter = ('brand', 'model')
    search_fields = ('model',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'title')
    list_filter = ('car', 'title')
    search_fields = ('text', 'title')
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
