from django.db import models
from clientes.models import Cliente
class Tarefa(models.Model):
    responsavel = models.ForeignKey('auth.User', on_delete = models.CASCADE,
        related_name="responsavel")
    nome_tarefa = models.CharField(max_length=100)
    descricao_tarefa = models.CharField(max_length=500)
    data_tarefa = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete =
            models.CASCADE,related_name='cliente')

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.data_tarefa)
