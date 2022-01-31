from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from . import models
import os
from django.conf import settings

def debug(*args):
    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
    for i in args:
        print(i)
    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')


class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'points', 'invited']

    class Meta:
        model = models.Users


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['category']

    class Meta:
        model = models.Categories


class ProductsImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'product']


class ProductFilesAdmin(admin.ModelAdmin):
    pass


class ProductImageInline(admin.StackedInline):
    model = models.ProductImages
    max_num = 10
    extra = 0

    readonly_fields = ['preview']
    def preview(self, obj):
        return mark_safe(f'<img src={str(obj)}>')
        # return mark_safe(f'<img src="{str(obj)}">')


class ProductFilesInline(admin.StackedInline):
    model = models.ProductFiles
    max_num = 10
    extra = 0


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity']
    inlines = [ProductImageInline, ProductFilesInline]

    class Meta:
        model = models.Products


class ArticleThemesAdmin(admin.ModelAdmin):
    list_display = ['theme']

    class Meta:
        model = models.ArticleThemes


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'theme']

    class Meta:
        model = models.Articles


class ReferralsAdmin(admin.ModelAdmin):
    list_display = ['id', 'referrer_id']

    class Meta:
        model = models.Referrals


class PurchasesAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'product_id', 'total', 'paid']

    class Meta:
        model = models.Purchases


class TestsQuestionsAdmin(admin.ModelAdmin):
    pass


class TestQuestionsInline(admin.StackedInline):
    model = models.TestsQuestions
    max_num = 30
    extra = 0


class TestsAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [TestQuestionsInline]

    class Meta:
        model = models.Tests


class TasksAdmin(admin.ModelAdmin):
    list_display = ['text', 'time', 'is_sent']

    class Meta:
        model = models.Tasks


admin.site.register(models.Users, UsersAdmin)
admin.site.register(models.ArticleThemes, ArticleThemesAdmin)
admin.site.register(models.Articles, ArticlesAdmin)
admin.site.register(models.Categories, CategoriesAdmin)
admin.site.register(models.ProductFiles, ProductFilesAdmin)
admin.site.register(models.ProductImages, ProductsImageAdmin)
admin.site.register(models.Products, ProductsAdmin)
admin.site.register(models.Referrals, ReferralsAdmin)
admin.site.register(models.Purchases, PurchasesAdmin)
admin.site.register(models.TestsQuestions, TestsQuestionsAdmin)
admin.site.register(models.Tests, TestsAdmin)
admin.site.register(models.Tasks, TasksAdmin)
