from django.urls import path
from catalogo.views import *
urlpatterns = [
    path('', index, name="index"),
    path('products/', list_produtos, name="list_produtos"),
    path('contact/', contact, name="contact"),
    path('produto/<int:produto_id>/', produto_detalhe, name='produto_detalhe'),

]
