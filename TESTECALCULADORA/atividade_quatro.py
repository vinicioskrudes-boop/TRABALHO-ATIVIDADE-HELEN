acervo = {}
emprestimos = {}
LIMITE = 3

def adicionar_livro(livro, exemplares):
    acervo[livro] = exemplares

def emprestar_livro(aluno, livro):
    if len(emprestimos.get(aluno, [])) >= LIMITE:
        return "limite"
    if acervo.get(livro, 0) <= 0:
        return "indisponivel"
    acervo[livro] -= 1
    emprestimos.setdefault(aluno, []).append(livro)
    return "ok"

def resetar_biblioteca():
    acervo.clear()
    emprestimos.clear()