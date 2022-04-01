#Classe Quadrado:Crie uma classe que modele um quadrado
#Atributos:
# - Tamanho do lado
#Métodos:
# - Mudar valor do Lado
# - Retornar valor do Lado
# - Calcular Área;

class Quadrado():
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado