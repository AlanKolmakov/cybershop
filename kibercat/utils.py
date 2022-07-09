from .models import *

menu = [
    {'index_name': 'Контакты', 'url_name': 'contacts'},
    {'index_name': 'Доставка и оплата', 'url_name': 'delivery'},
    {'index_name': 'Гарантия и возврат', 'url_name': 'warranty'},
    {'index_name': 'Бренды', 'url_name': 'brands'},
    {'index_name': 'Подобрать кресло', 'url_name': 'chairSelection'},
    {'index_name': 'Задайте вопрос', 'url_name': 'question'},
    {'index_name': 'Личный кабинет', 'url_name': 'auth'},
]


class DataMixin:
    def get_user_content(self, **kwargs):
        content = kwargs
        content['menu'] = menu
        content['slider_list'] = CaruselSlider.objects.all()
        content['best_obj'] = Product.objects.filter(bestseller__exact=True)[:4]
        content['new_obj'] = Product.objects.filter(novelty__exact=True)[:4]
        content['show_catalog'] = ProductCategory.objects.filter(is_active=True)
        return content
