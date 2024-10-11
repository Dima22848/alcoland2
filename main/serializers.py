from rest_framework import serializers
from .models import *


class AlcogolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer_characters
        fields = '__all__'