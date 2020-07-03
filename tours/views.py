from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError


class MainView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(
            request, r'tours\index.html')


class DepartureView(View):
    template_name = 'departure.html'

    def get(self, request):
        return render(
            request, r'tours\departure.html')


class TourView(View):
    template_name = "tour.html"

    def get(self, request):
        return render(
            request, r'tours\tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Такой страницы не существует')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
