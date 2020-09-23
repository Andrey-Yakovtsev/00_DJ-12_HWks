from django.shortcuts import render
from .models import Phone
from django.views.generic import ListView


# class PhoneListView(ListView):
#     Apple = Apple_brand.objects.all()[0]
#     Nokia = Nokia_brand.objects.all()[0]
#     Samsung = Samsung_brand.objects.all()[0]

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    # phones = [PhoneListView.Apple, PhoneListView.Nokia, PhoneListView.Samsung]
    # extras = Apple_brand.objects.all() and Samsung_brand.objects.all() and Nokia_brand.objects.all()
    context = {'phones': phones,
               # 'phones_values': phones.values(),
               # 'phones_values_list': phones.values_list(),
               # 'extras': extras.values()
               }
    return render(
        request,
        template,
        context
    )
