from django.contrib import admin
from .models import Tarefa
from django.contrib.admin import DateFieldListFilter
from django.contrib.auth.models import User

class TarefaContribute(admin.ModelAdmin):
    list_display = ['data_tarefa','nome_tarefa','responsavel','cliente',]
    search_fields = ('cliente__name','data_tarefa','responsavel__username',)
    list_filter = (
        ('data_tarefa', DateFieldListFilter),
    )


admin.site.register(Tarefa,TarefaContribute)

    # Register your models here.
