from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')
    group = models.CharField(max_length=200, db_index=True, verbose_name='Группа', blank=True)
    image = models.ImageField(upload_to='products_images/Catalog', verbose_name='Фото', blank=True)
    image_on_main = models.ImageField(upload_to='products_images/Catalog', verbose_name='Фото', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, blank=True, null=True, default=None)
    name = models.CharField(max_length=64, db_index=True, verbose_name='Название')
    article_name = models.CharField(max_length=64, db_index=True, verbose_name='Артикул')
    discount = models.IntegerField(default=0, verbose_name='Скидка %')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='URL')
    short_description = models.TextField(blank=True, verbose_name='Описание')
    full_description = models.TextField(blank=True, verbose_name='Характеристики')
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Остаток')
    is_active = models.BooleanField(default=True, verbose_name='Доступность')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    bestseller = models.BooleanField(default=False, verbose_name='Хит продаж')
    novelty = models.BooleanField(default=False, verbose_name='Новинка')
    image = models.ImageField(upload_to='products_images/', verbose_name='Фото', blank=True)
    rating = models.IntegerField(blank=True, verbose_name='Рейтинг', default=5)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Каталог товара'
        verbose_name_plural = 'Каталог товаров'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)


class ProductBrands(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products_images/Brands/', verbose_name='Фото')
    brands = models.CharField(max_length=64, db_index=True, verbose_name='Название')

    def __str__(self):
        return "%s" % self.pk

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class CaruselSlider(models.Model):
    carusel_img = models.ImageField(upload_to='slider_image')
    carusel_title = models.CharField(max_length=255, blank=True, verbose_name='Заголовок')
    carusel_text = models.CharField(max_length=255, blank=True, verbose_name='Текст')
    carusel_css = models.CharField(max_length=255, null=True, default='-', verbose_name='CSS класс')
    url = models.CharField(max_length=200, db_index=True, verbose_name='URL', blank=True)

    def __str__(self):
        return self.carusel_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
