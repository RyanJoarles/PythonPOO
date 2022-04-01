'''
Classe Pessoa: Crie uma classe que modele uma pessoa
    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer.

Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1

    def engordar(self):
        self.peso = self.peso + 3.125

    def emagrecer(self):
        self.peso = self.peso - 0.05

    def crescer(self):
        if self.idade < 21:
            self.altura = self.altura + 0.05

    #Getters e Setters(Corrigem os "kg" e "m" em peso e altura)
    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('kg', ''))
        self._peso = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('m', ''))
        self._altura = valor

p1 = Pessoa('Ryan', 12, '60kg', '1.38m')
print(p1.nome, p1.idade, p1.peso, p1.altura)

for i in range(8):
    p1.envelhecer()
    p1.crescer()
    p1.engordar()
    print(p1.nome, p1.idade, p1.peso, '{:.2f}'.format(p1.altura))



