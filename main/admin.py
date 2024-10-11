from django.contrib import admin
from .models import Category, Beer_characters, Vine_characters, Vodka_characters, Whiskey_characters, Cognak_characters

admin.site.register(Beer_characters)
admin.site.register(Vine_characters)
admin.site.register(Vodka_characters)
admin.site.register(Whiskey_characters)
admin.site.register(Cognak_characters)
admin.site.register(Category)

from django.core.files.base import ContentFile