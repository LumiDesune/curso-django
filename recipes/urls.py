from django.urls import path
from . import views

# ex: meusite.com/sobre -> roteamento do app
urlpatterns = [
    path('', views.home), # /recipes/ -> raiz
    path('sobre/', views.sobre), # /recipes/sobre -> página sobre
    path('contato/', views.contato),
    path('users/', views.users),
    path('list/', views.user_list)
]
