
import csv
from phones.models import Phone

# import os
# print(os.path.dirname(os.path.realpath(__file__)))
def handle():
    with open('phones.csv', 'r') as fo:
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

handle()
