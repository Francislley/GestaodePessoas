from django.db import models

# Create your models here.

class pessoa(models.Model):         #Cria a classe pessoa correspondente a tabela pessoa do BD
    nome = models.CharField(max_length=100)       # Cria a variável nome usando a classe models do Django como herança - Charfield = Varchar
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    dat_nasc = models.DateField()
