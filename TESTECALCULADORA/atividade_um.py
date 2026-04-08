USUARIOS = {"aluno01": "senha123", "professor": "prof@2024"}

def fazer_login(usuario, senha):
    if not usuario or not senha:
        return "campos_vazios"
    if usuario not in USUARIOS:
        return "usuario_invalido"
    if USUARIOS[usuario] != senha:
        return "senha_incorreta"
    return "ok"