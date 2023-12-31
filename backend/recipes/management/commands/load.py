import os
import csv

from django.core.management.base import BaseCommand
from recipes.models import Ingredient, Tag

Tags_data = (
    {'name': 'Крепкие', 'color': '#E26C2D', 'slug': 'strong'},
    {'name': 'Слабоалкогольные', 'color': '#8775D2', 'slug': 'low'},
    {'name': 'Безалкогольные', 'color': '#49B64E', 'slug': 'none'},
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        path = os.path.join('data', 'ingredients.csv')
        print('File path: ', path)

        with open(path) as f:
            reader = csv.reader(f)
            keys = ['name', 'measurement_unit']
            for row in reader:
                _, created = Ingredient.objects.get_or_create(
                    **dict(zip(keys, row))
                )

        for tag_data in Tags_data:
            _, created = Tag.objects.get_or_create(**tag_data)

        return print('Загрузка данных Ingredient и Tag готова!')
