from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError
import tours.data as data
import random


class MainView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        random_tours = random.sample(list(data.tours.items()), 6)

        return render(
            request, r'tours\index.html', {'title': data.title,
                                           'description': data.description,
                                           'subtitle': data.subtitle,
                                           'tours': dict(random_tours),
                                           'departures': data.departures})


class DepartureView(View):
    template_name = 'departure.html'

    def get(self, request, departure: str, *args, **kwargs):
        tourcount = 0
        price_list = []
        nights_list = []
        for number, tour in data.tours.items():
            if departure == tour['departure']:
                price_list.append(tour['price'])
                nights_list.append(tour['nights'])
                tourcount += 1

        return render(
            request, r'tours\departure.html', {'title': data.title,
                                               'tours': data.tours,
                                               'departures': data.departures,
                                               'from': data.departures[departure][3:],
                                               'departure': departure,
                                               'tourcount': tourcount,
                                               'pricemin': min(price_list),
                                               'pricemax': max(price_list),
                                               'nightsmin': min(nights_list),
                                               'nightsmax': max(nights_list)})


class TourView(View):
    template_name = "tour.html"

    def get(self, request, id: int):
        return render(
            request, r'tours\tour.html',
            {'title': data.title,
             'tours': data.tours[id],
             'departures': data.departures,
             'departure': data.departures[data.tours[id]['departure']]})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Такой страницы не существует')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
