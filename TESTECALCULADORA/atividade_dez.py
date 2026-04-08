turmas = {}

def cadastrar_turma(curso, turma, vagas):
    turmas[(curso, turma)] = {"vagas": vagas, "alunos": []}

def matricular_aluno(aluno, curso, turma):
    t = turmas.get((curso, turma))
    if not t:
        return "nao_encontrada"
    if len(t["alunos"]) >= t["vagas"]:
        return "lotada"
    t["alunos"].append(aluno)
    return "ok"

def resetar_turmas():
    turmas.clear()