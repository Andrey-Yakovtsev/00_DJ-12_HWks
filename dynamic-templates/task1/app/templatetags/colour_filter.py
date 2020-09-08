import csv

from django.template import library

register = library.Library()

@register.filter()
def get_colour(value):

    if value != '-':
        if float(value) > 1990:
            return "White"
        elif float(value) < 0:
            return 'Green'
        elif 1 < float(value) < 2:
            return 'LightSalmon'
        elif 2 < float(value) < 5:
            return 'Salmon'
        elif float(value) > 5:
            return 'Red'
    else:
        pass

@register.filter()  # Это фильтр для крайних столбцов. Доделать...
def make_gray(value):

    if value:
        return "Grey"