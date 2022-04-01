class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco - (self.preco * percentual / 100)

    #Getter e Setter são como um tipo de filtro de dados.
    # Impedem que informações erradas percorram pelo código

    #Getter
    @property
    def nome(self):
        return self._nome

    #Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('A', '@')

    #Getter
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('Blusa', 100)
print(f'Preço normal: {p1.preco}')
print(f'Preço com desconto: {p1.desconto(10)}\n')

p2 = Produto('Jaqueta', 'R$50')
print(f'Preço normal: {p2.preco}')
print(f'Preço com desconto: {p2.desconto(10)}')