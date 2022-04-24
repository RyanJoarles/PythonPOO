from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 120)
p2 = Produto('Jaqueta', 229.99)
p3 = Produto('Calca', 140)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(carrinho.soma_total())