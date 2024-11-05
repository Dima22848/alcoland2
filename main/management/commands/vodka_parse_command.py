import csv
from django.core.management.base import BaseCommand

from main.models import Vodka_characters
from main.parse.vodka import vodka_parse


class Command(BaseCommand):
    help = 'Export products data to a CSV file'

    def handle(self, *args, **kwargs):
        vodka_parse.vodka_array()
        for x in vodka_parse.vodka_list:
            Vodka_characters.objects.create(name=x[0],
                                            price=x[1],
                                            brand=x[2],
                                            country=x[3],
                                            volume=x[4],
                                            amount_in_box=x[5],
                                            vid=x[6],
                                            strength=x[7],
                                            excerpt=x[8],
                                            supply_temperature=x[9],
                                            taste=x[10],
                                            color=x[11],
                                            coctails=x[12],
                                            gastronomic_compatibility=x[13],
                                            sizes=x[14],
                                            weight=x[15],
                                            description=x[16],
                                            image=x[17])

        # Открываем файл для записи данных
        with open('vodka_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Записываем заголовки
            writer.writerow(['name',
                             'price',
                             'brand',
                             'country',
                             'volume',
                             'amount_in_box',
                             'vid',
                             'strength',
                             'excerpt',
                             'supply_temperature',
                             'taste',
                             'color',
                             'coctails',
                             'gastronomic_compatibility',
                             'sizes',
                             'weight',
                             'description'
                             ])

            vodkas = Vodka_characters.objects.all().values_list('name',
                                                                'price',
                                                                'brand',
                                                                'country',
                                                                'volume',
                                                                'amount_in_box',
                                                                'vid',
                                                                'strength',
                                                                'excerpt',
                                                                'supply_temperature',
                                                                'taste',
                                                                'color',
                                                                'coctails',
                                                                'gastronomic_compatibility',
                                                                'sizes',
                                                                'weight',
                                                                'description')

            # Записываем каждую запись в файл
            for vodka in vodkas:
                writer.writerow(vodka)

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))