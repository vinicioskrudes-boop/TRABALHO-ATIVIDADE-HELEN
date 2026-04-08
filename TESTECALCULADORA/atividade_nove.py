def transferir(saldo_origem, saldo_destino, valor, mesma_conta=False):
    if mesma_conta:
        return "mesma_conta", saldo_origem, saldo_destino
    if valor < 0:
        return "valor_negativo", saldo_origem, saldo_destino
    if valor == 0:
        return "valor_zero", saldo_origem, saldo_destino
    if saldo_origem < valor:
        return "saldo_insuficiente", saldo_origem, saldo_destino
    return "ok", saldo_origem - valor, saldo_destino + valor