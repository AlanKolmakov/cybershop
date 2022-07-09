from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import *
from .utils import *
from .models import *


# Главная страница
class KibercatMainPage(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/main.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Киберспортивный магазин для геймеров KiberCat.ru')
        return dict(list(content.items()) + list(c_def.items()))


class Contacts(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/contacts.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='KIBERCAT.RU - контакты, режим работы интернет магазина...')
        return dict(list(content.items()) + list(c_def.items()))


class Delivery(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/delivery.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='KIBERCAT.RU - условия доставки')
        return dict(list(content.items()) + list(c_def.items()))


class Warranty(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/warranty.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='KIBERCAT.RU - условия гарантии, обмена и возврата...')
        return dict(list(content.items()) + list(c_def.items()))


class Payments(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/payments.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='KIBERCAT.RU - условия оплаты заказа в интернет-магазине kibercat.ru')
        return dict(list(content.items()) + list(c_def.items()))


class Brands(DataMixin, ListView):
    model = ProductBrands
    template_name = 'kibercat/brands.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='KIBERCAT.RU - популярные бренды товаров...')
        return dict(list(content.items()) + list(c_def.items()))


class Info(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/info.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='KIBERCAT.RU - информация...')
        return dict(list(content.items()) + list(c_def.items()))


class ChairSelection(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/chairSelection.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Подбор кресла')
        return dict(list(content.items()) + list(c_def.items()))


class Question(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/question.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Задать вопрос')
        return dict(list(content.items()) + list(c_def.items()))


class ShowProduct(DataMixin, DetailView):
    model = Product
    template_name = 'kibercat/showProduct.html'
    context_object_name = 'object'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['rating'] = [n for n in range(5)]
        c_def = self.get_user_content(title=content['object'].name)
        return dict(list(content.items()) + list(c_def.items()))


class CatalogKresla(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Кресла', cat_selected=ProductCategory.objects.get(pk=1),
                                      cat_group=ProductCategory.objects.get(pk=11))
        return dict(list(content.items()) + list(c_def.items()))


class Catalog_Kresla_i_stoly(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog_group.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Кресла и Столы', cat_group_all=ProductCategory.objects.filter(group=1),
                                      cat_group=ProductCategory.objects.get(pk=11))
        return dict(list(content.items()) + list(c_def.items()))


class CatalogTable(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Столы', cat_selected=ProductCategory.objects.get(pk=2),
                                      cat_group=ProductCategory.objects.get(pk=11))
        return dict(list(content.items()) + list(c_def.items()))


class Cases(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Корпуса', cat_selected=ProductCategory.objects.get(pk=9),
                                      cat_group=ProductCategory.objects.get(pk=12))
        return dict(list(content.items()) + list(c_def.items()))


class PC_accessories(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog_group.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Комплектующие для ПК',
                                      cat_group_all=ProductCategory.objects.filter(group=2),
                                      cat_group=ProductCategory.objects.get(pk=12))
        return dict(list(content.items()) + list(c_def.items()))


class CatalogAksessuary(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Аксессуары', cat_selected=ProductCategory.objects.get(pk=3),
                                      cat_group=ProductCategory.objects.get(pk=11))
        return dict(list(content.items()) + list(c_def.items()))


class Power_supplies(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Блоки Питания', cat_selected=ProductCategory.objects.get(pk=10),
                                      cat_group=ProductCategory.objects.get(pk=12))
        return dict(list(content.items()) + list(c_def.items()))


class Cooling_systems(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Системы охлаждения', cat_selected=ProductCategory.objects.get(pk=13),
                                      cat_group=ProductCategory.objects.get(pk=12))
        return dict(list(content.items()) + list(c_def.items()))


class CatalogGarnitury(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Гарнитуры', cat_selected=ProductCategory.objects.get(pk=5),
                                      cat_group=ProductCategory.objects.get(pk=14))
        return dict(list(content.items()) + list(c_def.items()))


class Gaming_peripherals(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog_group.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Периферии', cat_group_all=ProductCategory.objects.filter(group=3),
                                      cat_group=ProductCategory.objects.get(pk=14))
        return dict(list(content.items()) + list(c_def.items()))


class CatalogMouse(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Мыши', cat_selected=ProductCategory.objects.get(pk=6),
                                      cat_group=ProductCategory.objects.get(pk=14))
        return dict(list(content.items()) + list(c_def.items()))


class CatalogKeyboard(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Клавиатуры', cat_selected=ProductCategory.objects.get(pk=7),
                                      cat_group=ProductCategory.objects.get(pk=14))
        return dict(list(content.items()) + list(c_def.items()))


class CatalogRugs(DataMixin, ListView):
    model = Product
    template_name = 'kibercat/catalog.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Каталог Коврики', cat_selected=ProductCategory.objects.get(pk=8),
                                      cat_group=ProductCategory.objects.get(pk=14))
        return dict(list(content.items()) + list(c_def.items()))


class Auth(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'kibercat/auth.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Авторизация')
        return dict(list(content.items()) + list(c_def.items()))


class Registration(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'kibercat/registration.html'
    success_url = reverse_lazy('auth')

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Регистрация')
        return dict(list(content.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('auth')
