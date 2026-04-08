carrinho = {}

def adicionar_produto(produto, preco, qtd=1):
    if produto in carrinho:
        carrinho[produto] = (preco, carrinho[produto][1] + qtd)
    else:
        carrinho[produto] = (preco, qtd)

def remover_produto(produto):
    carrinho.pop(produto, None)

def alterar_quantidade(produto, qtd):
    if produto in carrinho:
        carrinho[produto] = (carrinho[produto][0], qtd)

def total_carrinho():
    return sum(p * q for p, q in carrinho.values())

def limpar_carrinho():
    carrinho.clear()