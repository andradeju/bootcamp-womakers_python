from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest

@pytest.fixture
def curso():
  curso = baker.make(
    Curso,
    titulo = 'Java',
    data_curso = date.today(),
    carga_horaria = '44'
  ) 
  return curso


@pytest.mark.django_db
def test_str_deve_retornar_string_formatada(curso):
  assert str(curso) == 'Java: 2023-10-16 - 44'

