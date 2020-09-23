from django.shortcuts import render
from .models import Phone



def show_catalog(request):
    template = 'catalog.html'
    parameter = list(request.GET.keys())
    sorter = {
        'price.desc': Phone.objects.order_by('-price'),
         'price.asc': Phone.objects.order_by('price'),
         'name.desc': Phone.objects.order_by('-name'),
         'name.asc': Phone.objects.order_by('name')
    }

    context = {'phones': sorter[parameter[0]]}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_model = Phone.objects.filter(slug__iexact=slug)
    print(phone_model.values())
    context = {'phone': phone_model.values()}
    return render(request, template, context)
