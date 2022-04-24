class Escritor:
    def __init__(self, nome):
        self.__nome = nome  # Criei um Setter(Atributo privado)
        self.__ferramenta = None

    # Criando um Getter para permitir o acesso ao atributo privado fora da classe
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta escrevendo ...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina escrevendo ...')