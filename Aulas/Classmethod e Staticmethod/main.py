from random import randint

class Pessoa():
    anoAtual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Método de instância(Utiliza atributos definidos fora da classe)
    def get_nascimento(self):
        print(f'Ano de nascimento: {self.anoAtual - self.idade}')

    #Método de classe(Utiliza utiliza métodos globais referentes à classe)
    @classmethod
    def por_ano_nascimento(cls, nome, nascimento):
        idade = cls.anoAtual - nascimento
        return cls(nome, idade)

    #Função normal que permanece dentro da classe por motivos de organização
    @staticmethod
    def gera_id():
        rand = randint(1111, 1999)
        return rand

p1 = Pessoa.por_ano_nascimento('Ryan', 2001)
print(f'Idade: {p1.idade}')
p1.get_nascimento()
print(f'ID: {Pessoa.gera_id()}')

