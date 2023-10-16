from django import forms
from cursos.models import Curso
from datetime import date

class CursoForm(forms.ModelForm):
  def clean_data_curso(self):
    data_curso = self.cleaned_data['data_curso']
    hoje = date.today() 
    if data_curso < hoje:
      raise forms.ValidationError('Não é possível cadastrar um curso no passado')
    return data_curso  
  class Meta:
    model = Curso
    fields = ['titulo', 'nivel', 'carga_horaria','data_curso','descricao']