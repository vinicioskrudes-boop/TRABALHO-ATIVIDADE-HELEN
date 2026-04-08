import time

codigos = {}

def solicitar_codigo(email):
    if not email or "@" not in email:
        return False
    codigos[email] = ("123456", time.time())
    return True

def validar_codigo(email, codigo):
    if email not in codigos:
        return "sem_codigo"
    cod, ts = codigos[email]
    if time.time() - ts > 300:
        return "expirado"
    return "ok" if cod == codigo else "invalido"