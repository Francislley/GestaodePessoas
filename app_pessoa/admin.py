from django.contrib import admin

# Register your models here.
from app_pessoa.models import pessoa


class pessoaadmin(admin.ModelAdmin): #solicita a herança da classe pessoa
    list_display = ('nome', 'cpf') #lista apenas as variáveis solicitadas

admin.site.register(pessoa, pessoaadmin) #registra a classe no Admin do Django