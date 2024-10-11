from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *

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