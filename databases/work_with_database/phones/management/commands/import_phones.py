from django.core.management.base import BaseCommand
import csv
from phones.models import Phone


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('phones/phones.csv', 'r') as fo: #'../../phones.csv'
            phonedict = csv.DictReader(fo, delimiter=';')
            for phone in phonedict:
                unit = Phone.objects.get_or_create(
                    id=phone['id'],
                    name=phone['name'],
                    price=phone['price'],
                    image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug=phone['name'].replace(' ', '-')
                )
