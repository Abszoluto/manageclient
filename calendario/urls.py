from django.urls import path
from . import views

urlpatterns = [
    path('calendario/new/', views.new_tarefa, name='new_tarefa'),
    path('calendario/see/', views.today_task, name='today_task'),
]
