from django.shortcuts import render
from .models import Phone



def show_catalog(request):
    template = 'catalog.html'
    phones_models = Phone.objects.all()
    if 'price.desc' in request.GET:
       phones_models = Phone.objects.order_by('-price')
    if 'price.asc' in request.GET:
       phones_models = Phone.objects.order_by('price')
    if 'name.desc' in request.GET:
       phones_models = Phone.objects.order_by('-name')
    if 'name.asc' in request.GET:
       phones_models = Phone.objects.order_by('name')

    context = {'phones': phones_models}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_model = Phone.objects.filter(slug__iexact=slug)
    print(phone_model.values())
    context = {'phone': phone_model.values()}
    return render(request, template, context)
