from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=+100, verbose_name="Nome da pessoa")
    cpf = models.CharField(max_length=+100, verbose_name="CPF")
    num_sus = models.CharField(max_length=+100, verbose_name="Númro do SUS")
    telefone = models.CharField(max_length=+100, verbose_name="Númro de telefone")

    class Meta:
        verbose_name_plural = "Pessoa"

    def __str__(self):
        return f'{self.nome} {self.cpf} {self.num_sus} {self.telefone}' 

class Posto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do posto")

    class Meta:
        verbose_name_plural = "Posto"

    def __str__(self):
        return f'{self.nome}' 
    
class Area(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da area")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Area"

    def __str__(self):
        return f'{self.nome}'
    
class Medico(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do medico")
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Medico"

    def __str__(self):
        return f'{self.nome}'
    
class Horario(models.Model):
    horario = models.DateField(verbose_name="Horario para consulta")

    class Meta:
        verbose_name_plural = "Horario"

    def __str__(self):
        return f'{self.nome}'
    
class Consulta(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do medico")
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Medico"

    def __str__(self):
        return f'{self.nome}'
    


    
# Create your models here.
