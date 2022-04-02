'''
Tornar intâncias/funções/métodos inutilizáveis em outras partes do código.
. public (Podem ser acessados dentro e fora da classe)
._ private/protected (public _) Não impede de ser utilizado, apenas oculta da sugestão.
.__ private(Impede totalmente de ser utilizado fora da classe)
    Só pode ser acessado utilizando (_NOMECLASSE__nomeatributo)
'''

class BaseDeDados():
    def __init__(self):
        self.__dados = {}

    #O property permite que o .__dados seja acessado fora do código, mas não alterado.
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Lucas')
bd.inserir_cliente(2, 'Felipe')
bd.inserir_cliente(3, 'Caio')
bd.inserir_cliente(4, 'Guilherme')

bd.apaga_cliente(1)
bd.lista_clientes()
print(bd.dados)
#bd.dados = 'Tentando alterar'
# can't set attribute
