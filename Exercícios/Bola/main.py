#Classe Bola: Crie uma classe que modele uma bola
# Atributos:
# - Cor
# - Circunferência
# - Material
# Métodos:
# - TrocarCor
# - MostrarCor

from Bola import Bola

def main():
    b1 = Bola('Amarela', 50, 'Metal')
    b1.trocaCor('Azul')
    print(b1.mostraCor())

if __name__ == '__main__':
    main()