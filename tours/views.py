import random

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from tours import data


class MainView(View):

    def get(self, request, *args, **kwargs):
        tours_quantity = 6
        random_tours = random.sample(list(data.tours.items()), tours_quantity)

        return render(
            request, 'tours/index.html', {'title': data.title,
                                           'description': data.description,
                                           'subtitle': data.subtitle,
                                           'tours': dict(random_tours),
                                           'departures': data.departures})


class DepartureView(View):

    def get(self, request, departure: str, *args, **kwargs):
        tour_count = 0
        price_list = []
        nights_list = []
        for number, tour in data.tours.items():
            if departure == tour['departure']:
                price_list.append(tour['price'])
                nights_list.append(tour['nights'])
                tour_count += 1

        return render(
            request, 'tours/departure.html', {'title': data.title,
                                               'tours': data.tours,
                                               'departures': data.departures,
                                               'from': data.departures[departure][3:],
                                               'departure': departure,
                                               'tour_count': tour_count,
                                               'pricemin': min(price_list),
                                               'pricemax': max(price_list),
                                               'nightsmin': min(nights_list),
                                               'nightsmax': max(nights_list)})


class TourView(View):

    def get(self, request, id: int):
        return render(
            request, 'tours/tour.html',
            {'title': data.title,
             'tours': data.tours[id],
             'departures': data.departures,
             'departure': data.departures[data.tours[id]['departure']]})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Такой страницы не существует')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
