from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *


class AlcogolList(ListView):
    template_name = 'main/list.html'
    queryset = Category
    ALLOWED_VALUES = {
        'pivo': Beer_characters,
        'vino': Vine_characters,
        'cognac': Cognak_characters,
        'vodka': Vodka_characters,
        'whiskey': Whiskey_characters,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        q1_value = self.request.GET.get('q1', None)

        if q1_value not in self.ALLOWED_VALUES:
            q1_value = 'pivo'

        context['q1'] = q1_value

        ModelClass = self.ALLOWED_VALUES[q1_value]

        items = ModelClass.objects.all()

        # Реализуем пагинацию — 15 элементов на страницу
        paginator = Paginator(items, 15)

        # Получаем текущую страницу из GET-запроса (по умолчанию 1-я страница)
        page_number = self.request.GET.get('page', 1)

        # Получаем страницу с объектами
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj

        return context

    # def get(self, request, *args, **kwargs):
    #     alcogol_models = {
    #         'pivo': Beer_characters,
    #         'vino': Vine_characters,
    #         'cognac': Cognak_characters,
    #         'vodka': Vodka_characters,
    #         'whiskey': Whiskey_characters,
    #     }
    #
    #     alcohol_type_key = request.GET.get('q1', 'pivo')
    #     alcogol_type = alcogol_models.get(alcohol_type_key, Beer_characters)
    #
    #     # Получаем все обьекты выбранной категории алкоголя
    #     alcogol_list = alcogol_type.objects.all()
    #
    #     # Пагинация: 15 элементов на страницу
    #     paginator = Paginator(alcogol_list, 15)
    #     page = request.GET.get('page')
    #
    #     try:
    #         alcohols_paginated = paginator.page(page)
    #     except PageNotAnInteger:
    #         alcohols_paginated = paginator.page(1)
    #     except EmptyPage:
    #         alcohols_paginated = paginator.page(paginator.num_pages)
    #
    #     context = {
    #         'alcohol_list': alcohols_paginated,
    #         'alcohol_type': Category.objects.all(),
    #     }
    #
    #     return render(request, 'main/list.html', context)


class AlcogolDetail(DetailView):
    template_name = 'main/detail.html'















class AlcogolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = AlcogolSerializer

    @action(methods=['get'], detail=False)
    def beer(self, request):
        beer = Beer_characters.objects.order_by('id').values()
        beer_array = []
        for i in beer:
            i['image'] = 'http://127.0.0.1:8000/media/' + i['image']
            beer_array.append(i)
        return Response({'beer_characters':  beer_array})

    @action(methods=['get'], detail=False)
    def cognak(self, request):
        cognak = Cognak_characters.objects.order_by('id').values()
        cognak_array = []
        for i in cognak:
            i['image'] = 'http://127.0.0.1:8000/media/' + i['image']
            cognak_array.append(i)
        return Response({'cognak_characters': cognak_array})

    @action(methods=['get'], detail=False)
    def vine(self, request):
        vine = Vine_characters.objects.order_by('id').values()
        vine_array = []
        for i in vine:
            i['image'] = 'http://127.0.0.1:8000/media/' + i['image']
            vine_array.append(i)
        return Response({'vine_characters': vine_array})

    @action(methods=['get'], detail=False)
    def vodka(self, request):
        vodka = Vodka_characters.objects.order_by('id').values()
        vodka_array = []
        for i in vodka:
            i['image'] = 'http://127.0.0.1:8000/media/' + i['image']
            vodka_array.append(i)
        return Response({'vodka_characters': vodka_array})

    @action(methods=['get'], detail=False)
    def whiskey(self, request):
        whiskey = Whiskey_characters.objects.order_by('id').values()
        whiskey_array = []
        for i in whiskey:
            i['image'] = 'http://127.0.0.1:8000/media/' + i['image']
            whiskey_array.append(i)
        return Response({'whiskey_characters': whiskey})