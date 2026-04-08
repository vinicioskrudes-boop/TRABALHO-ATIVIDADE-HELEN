estoque = {}

def entrada_produto(produto, qtd):
    estoque[produto] = estoque.get(produto, 0) + qtd
    return estoque[produto]

def saida_produto(produto, qtd):
    if qtd > estoque.get(produto, 0):
        return False
    estoque[produto] -= qtd
    return estoque[produto]

def resetar_estoque():
    estoque.clear()