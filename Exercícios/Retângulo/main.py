'''
Classe Retangulo:Crie uma classe que modele um retangulo
 - Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
 - Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro

 - Crie  um  programa  que  utilize  esta  classe.
 Ele  deve  pedir  ao  usuário  que  informe  as  medidades  de  um  local.
 Depois,  deve  criar  um  objeto  com  as  medidas  e  calcular  a quantidade de pisos e
 de rodapés necessárias para o local.
'''

class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarLados(self, base, altura):
        self.base = base
        self.altura = altura
        return self.base, self.altura

    def calcularArea(self):
        area = self.base * self.altura
        return area

    def calcularPerimetro(self):
        perimetro = (self.base + self.altura) * 2
        return perimetro

r1 = Retangulo(2, 4)
b = int(input('Digite o valor da base: '))
a = int(input('Digite o valor da altura: '))
r1.mudarLados(b, a)
print(f'Base: {r1.base}\n'
      f'Altura: {r1.altura}'
      )
print(f'Área: {r1.calcularArea()}')
print(f'Perímetro: {r1.calcularPerimetro()}')



