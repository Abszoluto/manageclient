from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.cliente_list, name='cliente_list'),
    path('cliente/new/', views.cliente_new, name='cliente_new'),
]
