from django.db import models

# Create your models here.
class Curso(models.Model):
  niveis_curso = (
    ('Iniciante', 'Iniciante'),
    ('Intermediário', 'Intermediário'),
    ('Avançado', 'Avançado')
  )
  titulo = models.CharField(max_length=52)
  nivel = models.CharField(max_length=50, choices=niveis_curso)
  carga_horaria = models.IntegerField()
  data_curso = models.DateField(help_text='aaa/mm/dd')
  descricao = models.TextField()

  def __str__(self): 
    return f'{self.titulo}: {self.data_curso} - {self.carga_horaria}'


  class Meta:
    verbose_name = 'Cadastro de Curso'
    verbose_name_plural = 'Cadastros de Cursos'
    ordering = ['-data_curso']   
