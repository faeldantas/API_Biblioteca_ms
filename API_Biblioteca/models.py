from django.db import models
from rest_framework import serializers
# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    data_pub = models.PositiveIntegerField()
    categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
    
class Leitor(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.PositiveIntegerField() # restringir no serializer
    cidade = models.CharField(max_length=200)
    

    def __str__(self):
        return self.nome
    

class Emprestimo(models.Model):
    leitor = models.ForeignKey(Leitor, on_delete=models.DO_NOTHING)
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True)

    def __str__(self):
        return f'{self.leitor} - {self.livro}'



    
