from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name='Вид алкоголя')
    slug = models.SlugField(max_length=30, verbose_name='URL', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид алкоголя'
        verbose_name_plural = 'Виды алкоголя'

# class Image(models.Model):
#     # text = models.CharField(max_length=100)
#     image = models.ImageField(upload_to=f'photos/%Y/%m/%d/', verbose_name='Изображение', max_length=10000)
class Beer_characters(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    country_color_vid = models.CharField(max_length=150, verbose_name='Страна, цвет, вид')
    strength = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Крепость')
    bitterness = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='Горечь')
    density = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='Плотность')
    favor = models.CharField(max_length=400, verbose_name='Аромат')
    taste = models.CharField(max_length=400, verbose_name='Вкус')
    aftertaste = models.CharField(max_length=400, verbose_name='Послевкусие')
    composition = models.CharField(max_length=400, verbose_name='Композиция')
    is_combined = models.CharField(max_length=400, verbose_name='С чем сочетается')
    country = models.CharField(max_length=60,verbose_name='Страна')
    type = models.CharField(max_length=60,verbose_name='Тип')
    vid = models.CharField(max_length=60, verbose_name='Вид')
    color = models.CharField(max_length=60, verbose_name='Цвет')
    image = models.ImageField(upload_to=f'photos/Пиво/%Y/%m/%d/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пиво'
        verbose_name_plural = 'Пиво'

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": 'pivo', "pk": self.pk})

class Cognak_characters(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    code = models.CharField(max_length=10, verbose_name='Код товара')
    volume = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Объем')
    brand = models.CharField(max_length=60, verbose_name='Бренд')
    country = models.CharField(max_length=60, verbose_name='Страна')
    strength = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Крепость')
    excerpt = models.CharField(max_length=60, verbose_name='Выдержка', blank=True, null=True)
    production_area = models.CharField(max_length=100, verbose_name='Зона производства', blank=True, null=True)
    serving_temperature = models.IntegerField(verbose_name='Температура сервировки', blank=True, null=True)
    favor = models.CharField(max_length=150, verbose_name='Аромат', blank=True, null=True)
    taste = models.CharField(max_length=150, verbose_name='Вкус', blank=True, null=True)
    gastronomic_combination = models.CharField(max_length=150, verbose_name='Гастрономическое сочетание', blank=True, null=True)
    features_of_the_technology = models.CharField(max_length=200, verbose_name='Особенности технологии', blank=True, null=True)
    sort = models.CharField(max_length=150, verbose_name='Сорт винограда', blank=True, null=True)
    image = models.ImageField(upload_to=f'photos/Коньяк/%Y/%m/%d/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коньяк'
        verbose_name_plural = 'Коньяк'

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": 'cognac', "pk": self.pk})

class Vine_characters(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    color = models.CharField(max_length=60, verbose_name='Цвет', blank=True, null=True)
    country = models.CharField(max_length=60, verbose_name='Страна', blank=True, null=True)
    alcogol_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Алкоголь',blank=True, null=True)
    type = models.CharField(max_length=60, verbose_name='Тип', blank=True, null=True)
    brand = models.CharField(max_length=60, verbose_name='Бренд', blank=True, null=True)
    sugar = models.CharField(max_length=60, verbose_name='Сахар', blank=True, null=True)
    region = models.CharField(max_length=100, verbose_name='Регион', blank=True, null=True)
    style = models.CharField(max_length=60, verbose_name='Стиль', blank=True, null=True)
    sort = models.CharField(max_length=60, verbose_name='Сорт', blank=True, null=True)
    classification = models.CharField(max_length=150, verbose_name='Классификация', blank=True, null=True)
    image = models.ImageField(upload_to=f'photos/Вино/%Y/%m/%d/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вино'
        verbose_name_plural = 'Вино'

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": 'vino', "pk": self.pk})

class Vodka_characters(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    brand = models.CharField(max_length=60, verbose_name='Бренд')
    country = models.CharField(max_length=60, verbose_name='Страна-производитель товара', blank=True, null=True)
    volume = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Объем, л', blank=True, null=True)
    amount_in_box = models.IntegerField(verbose_name='Штук в ящике', blank=True, null=True)
    vid = models.CharField(max_length=60, verbose_name='Вид', blank=True, null=True)
    strength = models.IntegerField(verbose_name='Крепость', blank=True, null=True)
    excerpt = models.CharField(max_length=60, verbose_name='Выдержка', blank=True, null=True)
    supply_temperature = models.CharField(max_length=100, verbose_name='Температура подачи', blank=True, null=True)
    taste = models.CharField(max_length=200, verbose_name='Вкус', blank=True, null=True)
    color = models.CharField(max_length=60, verbose_name='Цвет', blank=True, null=True)
    coctails = models.CharField(max_length=150, verbose_name='Коктейли', blank=True, null=True)
    gastronomic_compatibility = models.CharField(max_length=200, verbose_name='Гастрономическая сочетаемость', blank=True, null=True)
    sizes = models.CharField(max_length=60, verbose_name='Размеры, см', blank=True, null=True)
    weight = models.CharField(max_length=60, verbose_name='Вес, кг', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to=f'photos/Водка/%Y/%m/%d/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Водка'
        verbose_name_plural = 'Водка'

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": 'vodka', "pk": self.pk})

class Whiskey_characters(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    brand = models.CharField(max_length=60, verbose_name='Бренд', blank=True, null=True)
    country = models.CharField(max_length=60, verbose_name='Страна производства', blank=True, null=True)
    vid = models.CharField(max_length=60, verbose_name='Вид напитка', blank=True, null=True)
    taste = models.CharField(max_length=250, verbose_name='Вкус', blank=True, null=True)
    favor = models.CharField(max_length=250, verbose_name='Аромат', blank=True, null=True)
    excerpt = models.CharField(max_length=150, verbose_name='Выдержка', blank=True, null=True)
    volume = models.IntegerField(verbose_name='Объем, мл', blank=True, null=True)
    strength = models.IntegerField(verbose_name='Крепость (% об.)', blank=True, null=True)
    fats = models.CharField(max_length=60, verbose_name='Жиры', blank=True, null=True)
    carbohydrates = models.CharField(max_length=60, verbose_name='Углеводы', blank=True, null=True)
    proteins = models.CharField(max_length=60, verbose_name='Белки', blank=True, null=True)
    calorie_content_kcal = models.CharField(max_length=60, verbose_name='Калорийность ккал', blank=True, null=True)
    humidity = models.CharField(max_length=60, verbose_name='Влажность', blank=True, null=True)
    storage_temperature = models.CharField(max_length=60, verbose_name='Температура хранения', blank=True, null=True)
    expiration_date = models.CharField(max_length=60, verbose_name='Срок годности', blank=True, null=True)
    storage_conditions = models.CharField(max_length=60, verbose_name='Условия хранения', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to=f'photos/Виски/%Y/%m/%d/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Виски'
        verbose_name_plural = 'Виски'

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": 'whiskey', "pk": self.pk})


