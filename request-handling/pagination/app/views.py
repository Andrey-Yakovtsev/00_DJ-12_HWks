from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse(bus_stations))

DATA = [str(i) for i in range (10000)]
def bus_stations(request):
    stations_list = []
    with open('data-398-2018-08-30.csv', encoding='cp1251', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations_list.append(row)
    paginator = Paginator(stations_list, 5)
    current_page = request.GET.get('page', 1)
    page_obj = paginator.get_page(current_page)
    # msg = '<br>'.join(page_obj.object_list)
    if page_obj.has_next():
        page_obj.next_page_number()
    if page_obj.has_previous():
        page_obj.previous_page_number()
    next_page_url = f'bus_stations?page={page_obj.next_page_number()}'
    previous_page_url = f'bus_stations?page={page_obj.previous_page_number()}'
    return render_to_response('index.html', context={
        'bus_stations': page_obj,
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

def get_data_from_csv(request):
    pass
