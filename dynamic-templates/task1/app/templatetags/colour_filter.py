import csv

from django.template import library

register = library.Library()

@register.filter()
def get_colour(value):
    with open("inflation_russia.csv", encoding="utf-8") as fo:
        read_csv = list(csv.reader(fo))
    table = [x.split(';') for b in read_csv for x in b]

    for name in table[1:]:
        if value == name[0]:
            return "White"
        if value == name[-1]:
            return "Grey"

    if value != '-':
        if float(value) < 0:
            return 'Green'
        elif 1 < float(value) < 2:
            return 'LightSalmon'
        elif 2 < float(value) < 5:
            return 'Salmon'
        elif float(value) > 5:
            return 'Red'
    else:
        pass