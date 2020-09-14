from django.contrib import admin
from .models import Phone, Apple_brand, Samsung_brand, Nokia_brand


class PhoneAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Apple_brand, BrandAdmin)
admin.site.register(Samsung_brand, BrandAdmin)
admin.site.register(Nokia_brand, BrandAdmin)
