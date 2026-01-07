from django.urls import path
from catalogo.views import *
urlpatterns = [
    path('', index, name="index"),
    path('products/', list_produtos, name="list_produtos"),
    path('contact/', contact, name="contact"),
    path('clique/<int:produto_id>', aumentar_click, name="clique"),
    path('clique_whatsapp/<int:produto_id>', aumentar_click_whatsapp, name="WhatsApp"),
    path('produto/<int:produto_id>/', produto_detalhe, name='produto_detalhe'),

]
