#Classe Bola: Crie uma classe que modele uma bola
# Atributos:
# - Cor
# - Circunferência
# - Material
# Métodos:
# - TrocarCor
# - MostrarCor

class Bola():
    def __init__(self, cor, circunf, material):
        self.cor = cor
        self.circunf = circunf
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor