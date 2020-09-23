from django.db import models


class Phone(models.Model):
    modelname = models.TextField(primary_key=True, serialize=False)
    brand = models.TextField(blank=True, default='')
    name = models.TextField(blank=True, default='')
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    model_year = models.CharField(max_length=4, blank=True, default='')
    has_camera = models.BooleanField(blank=True, null=True)
    camera_res = models.CharField(max_length=50, blank=True, default='')
    sim_type = models.TextField(blank=True, default='')
    dimensions = models.CharField(max_length=50, blank=True, default='')
    weight = models.CharField(max_length=10, blank=True, default='')
    battery_capacity = models.CharField(max_length=30, blank=True, default='')
    os_version = models.TextField(blank=True, default='')
    processor = models.TextField(blank=True, default='')
    gps_support = models.TextField(blank=True, default='')
    lte_exists = models.BooleanField(blank=True, null=True)
    fingerprint_scanner = models.BooleanField(blank=True, null=True)
    face_scanner = models.BooleanField(blank=True, null=True)
    color = models.TextField(blank=True, default='')
    slug = models.CharField(max_length=150, blank=True, default='')


class Apple_brand(models.Model):
    model = models.ForeignKey(Phone, on_delete=models.CASCADE, verbose_name='Название модели', related_name='+')
    extra = models.CharField(verbose_name="Дополнительно", max_length=200, blank=True, default='')


class Samsung_brand(models.Model):
    model = models.ForeignKey(Phone, on_delete=models.CASCADE, verbose_name='Название модели', related_name='+')
    extra = models.CharField(verbose_name="Дополнительно", max_length=200, blank=True, default='')


class Nokia_brand(models.Model):
    model = models.ForeignKey(Phone, on_delete=models.CASCADE, verbose_name='Название модели', related_name='+')
    extra = models.CharField(verbose_name="Дополнительно", max_length=200, blank=True, default='')
