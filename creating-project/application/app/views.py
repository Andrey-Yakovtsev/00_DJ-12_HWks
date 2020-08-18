import csv
import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


CSV_FILENAME = 'phones.csv'
COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]


def table_view(request):
    template = 'table.html'
    with open(CSV_FILENAME, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': COLUMNS, 
            'table': table, 
            'csv_file': CSV_FILENAME
        }
        result = render(request, template, context)
    return result

def current_time_view(request):
    current_time = datetime.now()
    return HttpResponse(f'Current time is: {current_time}')

def workdir_view(request):
    dirpath = os.listdir(path='.') #/home/ayakovtsev/PycharmProjects/00_DJ-12_HWks/dj-homeworks/creating-project/appliсation')
    return HttpResponse(list(dirpath))

def home_view(request):

    return HttpResponse('<h1>У нас есть следующие разделы:</h1>'
                        '<div></div><a href="/current_time">Текущее время</a>'
                        '<div></div><a href="/table">Табличка с телефонами</a>'
                        '<div></div><a href="/workdir">Список директорий и файлов проекта</a>')