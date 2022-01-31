from django.contrib.postgres.fields import JSONField
from django.db import models
from uuid import uuid4
from time import time
import os


class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


class Users(TimeBasedModel):
    """ Модель для хранения всех данный о пользователях телеграмма """

    user_id = models.BigIntegerField(verbose_name='ID пользователя в телеграмме', unique=True)
    name = models.CharField(verbose_name='Имя пользователя', max_length=255)
    email = models.EmailField(verbose_name='Email пользователя', blank=True)
    phone = models.CharField(verbose_name='Телефон пользователя', blank=True, max_length=255)
    invited = models.BooleanField(verbose_name='Пользователь был приглашен', default=False)
    points = models.BigIntegerField(verbose_name='Баллы пользователя', default=0)

    def __str__(self):
        return f'{self.name}:{self.user_id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Referrals(TimeBasedModel):
    """ Таблица с рефералами (пользователями, пришедшими от других пользователей) """

    id = models.ForeignKey(Users, primary_key=True,
                           on_delete=models.CASCADE)
    referrer_id = models.BigIntegerField(verbose_name='ID пользователя, который его привел')

    def __str__(self):
        return f'{self.id}:{self.referrer_id}'

    class Meta:
        verbose_name = 'Реферал'
        verbose_name_plural = 'Рефералы'


class Categories(TimeBasedModel):
    """ Таблица с категориями товаров """

    category = models.CharField(verbose_name='Категория', max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(TimeBasedModel):
    """ Модель для товаров """

    title = models.CharField(verbose_name='Название товара', max_length=255)
    description = models.TextField(verbose_name='Описание товара', max_length=400)
    category = models.ForeignKey(Categories, verbose_name='Категория товара',
                                 on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена товара', default=0)
    currency = models.CharField(verbose_name='Валюта', default='руб', max_length=100)
    quantity = models.BigIntegerField(verbose_name='Количестао товара', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split(".")[-1]
        # get filename
        filename = "{}_{}.{}".format(uuid4().hex, str(int(time())), ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper


class ProductFiles(TimeBasedModel):
    video = models.FileField(verbose_name='Видео для товара',
                             upload_to='bot/adminbot/media/products/', blank=True)

    video_unique_id = models.CharField(verbose_name='ID видеоролика', max_length=255,
                                       blank=True)

    caption = models.CharField(verbose_name='Подпись к видео', max_length=255,
                               blank=True)

    product = models.ForeignKey(Products,
                                related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.video)

    class Meta:
        verbose_name = 'Видео для товара'
        verbose_name_plural = 'Видео для товаров'


class ProductImages(TimeBasedModel):
    """ Таблица с изображениями для товаров """

    image = models.ImageField(verbose_name='Изображение товара',
                              upload_to='bot/adminbot/media/products/', blank=True)
    image_unique_id = models.CharField(verbose_name='ID файла', blank=True,
                                       max_length=255)
    caption = models.CharField(verbose_name='Подпись к фотографии', max_length=255,
                               blank=True)
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'


class Purchases(TimeBasedModel):
    """ Таблица с информацией о покупках """

    buyer = models.ForeignKey(Users, verbose_name='Покупатель', on_delete=models.SET(0))
    product_id = models.ForeignKey(Products, verbose_name='ID Товара', on_delete=models.CASCADE)
    total = models.DecimalField(verbose_name='Общая стоимость', decimal_places=2, max_digits=2)
    quantity = models.IntegerField(verbose_name='Количество товара')
    purchase_time = models.DateTimeField(verbose_name='Время покупки', auto_now_add=True)
    shipping_address = JSONField(verbose_name='Адрес доставки', null=True)
    buyer_phone = models.CharField(verbose_name='Телефон покупателя', max_length=100, null=True)
    buyer_email = models.CharField(verbose_name='Email покупателя', max_length=255, null=True)
    paid = models.BooleanField(verbose_name='Оплачено', default=False)

    def __str__(self):
        return f'{self.buyer}:{self.pk}:{self.product_id}:{self.quantity}'

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class ArticleThemes(TimeBasedModel):
    """ Таблица с темами для статей """

    theme = models.CharField(verbose_name='Тема статьи', max_length=255)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Тема статьи'
        verbose_name_plural = 'Темы статьи'


class Articles(TimeBasedModel):
    """ Таблица со статьями """

    title = models.CharField(verbose_name='Заголовок статьи', max_length=255)
    intro = models.TextField(verbose_name='Вступление', max_length=500, blank=True)
    text = models.TextField(verbose_name='Текст статьи')
    theme = models.ForeignKey(ArticleThemes, verbose_name='Тема статьи',
                              on_delete=models.CASCADE)
    author = models.CharField(verbose_name='Автор', max_length=255, blank=True)
    preview = models.ImageField(verbose_name='Превью статьи',
                                upload_to='bot/adminbot/media/articles/', blank=True)
    preview_id = models.TextField(blank=True)

    def __str__(self):
        return f'{self.pk}:{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Tests(TimeBasedModel):
    """ Таблица с тастами """

    name = models.CharField(verbose_name='Название теста', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тест'


class TestsQuestions(TimeBasedModel):
    """ Таблица с изображениями для товаров """

    data = models.TextField(verbose_name='Вопрос:варианты, ответа, через, запятую:ответ', )
    test = models.ForeignKey(Tests, related_name='tests', on_delete=models.CASCADE)

    def __str__(self):
        return f'Вопросы для: {self.test.name}'

    class Meta:
        verbose_name = 'Данные для теста'
        verbose_name_plural = 'Данные для теста'


class Tasks(TimeBasedModel):
    """ Таблица с информацией для рассылки всем пользователям """
    text = models.TextField(verbose_name='Текст')
    time = models.DateTimeField(verbose_name='Время и дата рассылки')
    is_sent = models.BooleanField(verbose_name='Сообщение отправлено',
                                  default=False)

    def __str__(self):
        return f'{self.text[:15]}_{self.time}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


