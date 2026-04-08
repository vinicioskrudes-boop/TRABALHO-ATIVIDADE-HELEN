import re

def cadastrar_cliente(nome, cpf, email, telefone):
    if not nome:
        return "nome_invalido"
    if not re.fullmatch(r"\d{11}", cpf or ""):
        return "cpf_invalido"
    if not email or "@" not in email:
        return "email_invalido"
    if not re.fullmatch(r"\d{10,11}", telefone or ""):
        return "telefone_invalido"
    return "ok"