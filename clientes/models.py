from django.db import models


class Cliente(models.Model):
    name = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField('E-MAIL',null=True)
    datanasc = models.DateField("Data de Nascimento")
    endereco = models.CharField(max_length=300)
    cpf = models.CharField('CPF', max_length=14)
    rg = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    telefone = models.CharField(max_length=11)

    def publish(self):
        self.save()
    def __str__(self):
        return f"{self.name} {self.sobrenome}"
