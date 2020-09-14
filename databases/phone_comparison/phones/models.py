from django.db import models


class Phone(models.Model):
    modelname = models.TextField(primary_key=True, serialize=False)
    brand = models.TextField(blank=True)
    name = models.TextField(blank=False)
    price = models.FloatField(blank=True)
    image = models.ImageField(blank=True)
    model_year = models.CharField(max_length=4, blank=True)
    has_camera = models.BooleanField(blank=True)
    camera_res = models.CharField(max_length=50, blank=True)
    sim_type = models.TextField(blank=True)
    dimensions = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=10, blank=True)
    battery_capacity = models.CharField(max_length=30, blank=True)
    os_version = models.TextField(blank=True)
    processor = models.TextField(blank=True)
    gps_support = models.TextField(blank=True)
    lte_exists = models.BooleanField(blank=True)
    fingerprint_scanner = models.BooleanField(blank=True)
    face_scanner = models.BooleanField(blank=True)
    color = models.TextField(blank=True)
    slug = models.CharField(max_length=150, blank=True, default='')


class Apple_brand(models.Model):
    model = models.ForeignKey(Phone, default='', on_delete=models.CASCADE, verbose_name='Название модели', related_name='+')
    display = models.CharField(max_length=100, default='', blank=True, null=True)
    giroscope = models.BooleanField(default=True, null=True)
    connection = models.CharField(max_length=100, default='', blank=True, null=True)


class Samsung_brand(models.Model):
    model = models.ForeignKey(Phone, default='', on_delete=models.CASCADE, verbose_name='Название модели', related_name='+')
    sound = models.TextField(default='')
    sd_card_support = models.BooleanField(default=True)


class Nokia_brand(models.Model):
    model = models.ForeignKey(Phone, default='', on_delete=models.CASCADE, verbose_name='Название модели', related_name='+')
    GPU = models.CharField(max_length=50)
