from django.shortcuts import render
from cursos.forms import CursoForm
from cursos.models import Curso
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(15)
def criar_curso(request):
  cursos = Curso.objects.all()
  form = CursoForm(request.POST or None)
  sucesso = False
  if form.is_valid():
    form.save()
    sucesso = True
  contexto = {
    'form': form,
    'sucesso': sucesso,
    'cursos': cursos,
  }
  return render(request, 'criar_curso.html', contexto)


