#Classe Quadrado:Crie uma classe que modele um quadrado
#Atributos:
# - Tamanho do lado
#Métodos:
# - Mudar valor do Lado
# - Retornar valor do Lado
# - Calcular Área;

from Quadrado import Quadrado

def main():
    q1 = Quadrado(2)
    q1.mudarLado(3)
    print(q1.calcularArea())

if __name__ == '__main__':
    main()