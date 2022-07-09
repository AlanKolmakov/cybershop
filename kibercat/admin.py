from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('article_name',)}
    list_display = ('name', 'article_name', 'image', 'category', 'discount', 'price', 'stock', 'bestseller', 'novelty', 'is_active',
                    'created')
    list_display_links = ('name',)
    search_fields = ('name', 'article_name')
    list_editable = ('bestseller', 'novelty', 'is_active',)
    list_filter = ('is_active', 'category', 'created', 'bestseller', 'novelty')


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('name',)
    search_fields = ('name',)


class ProductBrandsAdmin(admin.ModelAdmin):
    list_display = ('brands', 'image')
    list_display_links = ('brands',)


class CaruselSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'carusel_img', 'carusel_title', 'carusel_text', 'carusel_css')
    list_editable = ('carusel_text', 'carusel_css',)
    list_display_links = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductBrands, ProductBrandsAdmin)
admin.site.register(CaruselSlider, CaruselSliderAdmin)
