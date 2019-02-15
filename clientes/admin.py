from django.contrib import admin
from .models import Cliente 

class ClienteContribute(admin.ModelAdmin):
    list_display = ['name','sobrenome','telefone',]
    search_fields = ('name','sobrenome','cpf','rg',)
admin.site.register(Cliente, ClienteContribute)

