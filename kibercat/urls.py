from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', KibercatMainPage.as_view(), name='main'),
    path('kibercat/contacts/', Contacts.as_view(), name='contacts'),
    path('kibercat/help/delivery/', Delivery.as_view(), name='delivery'),
    path('kibercat/help/warranty/', Warranty.as_view(), name='warranty'),
    path('kibercat/info/brands/', Brands.as_view(), name='brands'),
    path('kibercat/info/', Info.as_view(), name='info'),
    path('kibercat/product/<slug:product_slug>/', ShowProduct.as_view(), name='product'),
    path('kibercat/help/payments/', Payments.as_view(), name='payments'),
    path('kibercat/podbor-kresla/', ChairSelection.as_view(), name='chairSelection'),
    path('kibercat/question/', Question.as_view(), name='question'),
    path('kibercat/catalog/igrovye-kresla-i-stoly/igrovye-kresla-/', CatalogKresla.as_view(), name='kompyuternye-kresla'),
    path('kibercat/catalog/igrovye-kresla-i-stoly/', Catalog_Kresla_i_stoly.as_view(), name='kompyuternye-kresla-i-stoly'),
    path('kibercat/catalog/igrovye-kresla-i-stoly/table/', CatalogTable.as_view(), name='kompyuternye-stoly'),
    path('kibercat/catalog/igrovye-kresla-i-stoly/aksessuary/', CatalogAksessuary.as_view(), name='aksessuary'),
    path('kibercat/catalog/komplektuyushchie-dlya-pk/korpusa/', Cases.as_view(), name='korpusa-dlya-pk'),
    path('kibercat/catalog/komplektuyushchie-dlya-pk/', PC_accessories.as_view(), name='komplektuyushie-dlya-pk'),
    path('kibercat/catalog/komplektuyushchie-dlya-pk/bloki_pitaniya-pk/', Power_supplies.as_view(), name='bloki-pitaniya'),
    path('kibercat/catalog/komplektuyushchie-dlya-pk/sistemy-ohlazhdeniya/', Cooling_systems.as_view(), name='sistemy-ohlazhdeniya'),
    path('kibercat/catalog/igrovaya-periferiya/garnitury/', CatalogGarnitury.as_view(), name='garnitury'),
    path('kibercat/catalog/igrovaya-periferiya/', Gaming_peripherals.as_view(), name='igrovaya-periferiya'),
    path('kibercat/catalog/igrovaya-periferiya/mouse/', CatalogMouse.as_view(), name='myshi'),
    path('kibercat/catalog/igrovaya-periferiya/keyboard/', CatalogKeyboard.as_view(), name='klaviatury'),
    path('kibercat/catalog/igrovaya-periferiya/rugs/', CatalogRugs.as_view(), name='kovriki-i-bunkery'),
    path('kibercat/auth/', Auth.as_view(), name='auth'),
    path('kibercat/registration/', Registration.as_view(), name='registration'),
    path('kibercat/logout/', auth_views.LogoutView.as_view(template_name='kibercat/auth.html'), name='logout'),
]
