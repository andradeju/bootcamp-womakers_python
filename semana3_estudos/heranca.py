class Pessoa:
  def __init__(self, nome):
    self._nome = nome
    self._tipo = 'Pessoa'

  def falar_oi(self):
    print('Oi! Meu nome é {}'.format(self._nome)) 

  def falar_tipo(self):
    print('Meu tipo é {}'.format(self._tipo))   

pessoa = Pessoa('Dora')
pessoa.falar_oi()
pessoa.falar_tipo()
print()    

class Estudante(Pessoa): # o nome da classe base vem em parênteses
  def __init__(self, nome, curso):
    super().__init__(nome) #chama o construtor da classe base
    self._curso = curso

  def falar_curso(self):
    print(f'Eu, {self._nome}, estudo o curso {self._curso}') # A propriedade self._nome é herdada da classe base

  def falar_tipo(self): #Sobescreve a função original da classe Pessoa
    self._tipo = 'Estudante'
    return super().falar_tipo()   

estudante = Estudante('Juca Westie', 'Introdução ao Python')
estudante.falar_oi() #o método "falar_oi" é herdado da classe base
estudante.falar_tipo() #o método "falar_tipo" é herdado da classe base, e sobescrita na classe derivada
estudante.falar_curso()   
print()

print('O objeto estudante é uma instância da classe Estudante?', isinstance(estudante, Estudante))
print('O objeto estudante é uma instância da classe Pessoa?', isinstance(estudante, Pessoa))
print('A classe Estudante é uma sub-classe de Pessoa?', issubclass(Estudante, Pessoa))
print('A classe Pessoa é uma sub-classe de Estudante?', issubclass(Pessoa, Estudante))


class Trabalhador(Pessoa): # Trabalhador também herda de Pessoa
  def __init__(self, nome, profissao):
    super().__init__(nome) #chama o construtor da classe base
    self._profissao = profissao # atributo privado - só pode ser acessado dentro da classe Trabalhador
    self._tipo = 'Trabalhador'

  def falar_profissao(self):
    print(f'Eu, {self._nome}, exerço a profissão {self._profissao}')

  def falar_tipo(self):
    return super().falar_tipo()

class Professor(Trabalhador):
  def __init__(self, nome, disciplina):
    super().__init__(nome, 'Professor') #chama o consructor da classe base
    self._disciplina = disciplina

  def falar_profissao(self):
    self.__profissao = 'Instrutora' # variaveis privadas não conseguem ser alteradas pela classe derivada
    return super().falar_profissao()          

  def falar_disciplina(self):
    print(f'Eu, {self._nome} dou aulas da disciplina {self._disciplina}')

  def falar_tipo(self):
    self._tipo = 'Professor'
    return super().falar_tipo()  

trabalhadora = Trabalhador('Juliana', 'Desenvolvedora')
trabalhadora.falar_oi()
trabalhadora.falar_tipo()
trabalhadora.falar_profissao()
print()    

professora = Professor('Nath', 'Python')
professora.falar_oi()
professora.falar_tipo()
professora.falar_profissao()
professora.falar_disciplina()
print()