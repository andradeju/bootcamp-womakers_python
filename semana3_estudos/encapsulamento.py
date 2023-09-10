class Pessoa:
    def __init__(self, nome, profissao, identidade):
        self._nome = nome
        self.profissao = profissao
        self.__identidade = identidade

    def __str__(self):
        return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self.__identidade}'

pessoal = Pessoa('Lady Lima', 'Astronauta', '12345')
print(pessoal)
print()

#Se tentarmos alterar um atributo publico, nós vamos conseguir
pessoal.profissao = "Desenvolvedora"
print(pessoal)
print()

#Se tentarmos alterar um atributo protegido, nós vamos conseguir também
pessoal._nome = 'Beyonce Ferreira'
print(pessoal)
print()

#Ao tentar um atributo privado, o valor não vai ser alterado
pessoal.__identidade = '54321'
print(pessoal)
print()