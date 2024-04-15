import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    with open(settings.BUS_STATION_CSV) as csvfile:
        reader = csv.DictReader(csvfile)
        stations = []
        for row in reader:
            stations.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page = request.GET.get('page', 1)
    bus_stations = Paginator(stations, 10).get_page(page)
   

    context = {
        'bus_stations': bus_stations,
    }
    return render(request, 'stations/index.html', context)
