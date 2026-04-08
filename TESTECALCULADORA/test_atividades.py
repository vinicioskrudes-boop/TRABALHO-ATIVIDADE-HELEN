# atividade 1

from atividade_um import fazer_login
import pytest

def test_login_correto():
    resultado = fazer_login("aluno01", "senha123")
    assert resultado == "ok"

def test_login_senha_incorreta():
    resultado = fazer_login("aluno01", "errada")
    assert resultado == "senha_incorreta"

def test_login_usuario_invalido():
    resultado = fazer_login("ninguem", "senha123")
    assert resultado == "usuario_invalido"

def test_login_usuario_vazio():
    resultado = fazer_login("", "senha123")
    assert resultado == "campos_vazios"

def test_login_senha_vazia():
    resultado = fazer_login("aluno01", "")
    assert resultado == "campos_vazios"

def test_login_ambos_vazios():
    resultado = fazer_login("", "")
    assert resultado == "campos_vazios"

# atividade 2

from atividade_dois import cadastrar_cliente
import pytest

def test_cadastro_valido():
    resultado = cadastrar_cliente("Ana", "12345678901", "ana@email.com", "44999990000")
    assert resultado == "ok"

def test_nome_vazio():
    resultado = cadastrar_cliente("", "12345678901", "ana@email.com", "44999990000")
    assert resultado == "nome_invalido"

def test_cpf_invalido():
    resultado = cadastrar_cliente("Ana", "123", "ana@email.com", "44999990000")
    assert resultado == "cpf_invalido"

def test_email_invalido():
    resultado = cadastrar_cliente("Ana", "12345678901", "semarroba", "44999990000")
    assert resultado == "email_invalido"

def test_telefone_invalido():
    resultado = cadastrar_cliente("Ana", "12345678901", "ana@email.com", "99")
    assert resultado == "telefone_invalido"

def test_todos_campos_vazios():
    resultado = cadastrar_cliente("", "", "", "")
    assert resultado == "nome_invalido"

# atividade 3

from atividade_tres import (adicionar_produto, remover_produto,
    alterar_quantidade, total_carrinho, limpar_carrinho)
import pytest

def test_adicionar_produto():
    limpar_carrinho()
    adicionar_produto("Caneta", 2.50)
    resultado = total_carrinho()
    assert resultado == 2.50

def test_adicionar_dois_produtos():
    limpar_carrinho()
    adicionar_produto("Caneta", 2.50)
    adicionar_produto("Caderno", 15.00)
    resultado = total_carrinho()
    assert resultado == 17.50

def test_remover_produto():
    limpar_carrinho()
    adicionar_produto("Caneta", 2.50)
    remover_produto("Caneta")
    resultado = total_carrinho()
    assert resultado == 0.0

def test_alterar_quantidade():
    limpar_carrinho()
    adicionar_produto("Caneta", 2.50, 1)
    alterar_quantidade("Caneta", 3)
    resultado = total_carrinho()
    assert resultado == 7.50

def test_carrinho_vazio():
    limpar_carrinho()
    resultado = total_carrinho()
    assert resultado == 0.0

def test_mesmo_produto_acumula():
    limpar_carrinho()
    adicionar_produto("Caneta", 2.50, 2)
    adicionar_produto("Caneta", 2.50, 1)
    resultado = total_carrinho()
    assert resultado == 7.50

# atividade 4

from atividade_quatro import adicionar_livro, emprestar_livro, resetar_biblioteca
import pytest

def test_emprestimo_disponivel():
    resetar_biblioteca()
    adicionar_livro("Python", 2)
    resultado = emprestar_livro("aluno1", "Python")
    assert resultado == "ok"

def test_emprestimo_indisponivel():
    resetar_biblioteca()
    adicionar_livro("Python", 0)
    resultado = emprestar_livro("aluno1", "Python")
    assert resultado == "indisponivel"

def test_limite_emprestimos():
    resetar_biblioteca()
    for l in ["L1", "L2", "L3", "L4"]:
        adicionar_livro(l, 1)
    for l in ["L1", "L2", "L3"]:
        emprestar_livro("aluno1", l)
    resultado = emprestar_livro("aluno1", "L4")
    assert resultado == "limite"

def test_estoque_decrementado():
    resetar_biblioteca()
    from atividade_quatro import acervo
    adicionar_livro("Python", 2)
    emprestar_livro("aluno1", "Python")
    resultado = acervo["Python"]
    assert resultado == 1

# atividade 5

from atividade_cinco import cadastrar_compromisso, limpar_agenda
import pytest

def test_compromisso_valido():
    limpar_agenda()
    resultado = cadastrar_compromisso("10/06/2025", "14:00", "Reunião")
    assert resultado == "ok"

def test_data_invalida():
    resultado = cadastrar_compromisso("99/99/9999", "14:00", "Reunião")
    assert resultado == "data_invalida"

def test_hora_invalida():
    resultado = cadastrar_compromisso("10/06/2025", "99:99", "Reunião")
    assert resultado == "hora_invalida"

def test_conflito_horario():
    limpar_agenda()
    cadastrar_compromisso("10/06/2025", "14:00", "Reunião")
    resultado = cadastrar_compromisso("10/06/2025", "14:00", "Outro")
    assert resultado == "conflito"

def test_horarios_diferentes():
    limpar_agenda()
    cadastrar_compromisso("10/06/2025", "14:00", "Reunião")
    resultado = cadastrar_compromisso("10/06/2025", "15:00", "Consulta")
    assert resultado == "ok"

# atividade 6

from atividade_seis import solicitar_codigo, validar_codigo, codigos
import pytest, time

def test_solicitar_codigo_valido():
    resultado = solicitar_codigo("user@email.com")
    assert resultado == True

def test_solicitar_codigo_email_invalido():
    resultado = solicitar_codigo("semarroba")
    assert resultado == False

def test_validar_codigo_correto():
    solicitar_codigo("user@email.com")
    resultado = validar_codigo("user@email.com", "123456")
    assert resultado == "ok"

def test_validar_codigo_incorreto():
    solicitar_codigo("user@email.com")
    resultado = validar_codigo("user@email.com", "000000")
    assert resultado == "invalido"

def test_validar_codigo_expirado():
    solicitar_codigo("user@email.com")
    codigos["user@email.com"] = ("123456", time.time() - 400)
    resultado = validar_codigo("user@email.com", "123456")
    assert resultado == "expirado"

def test_validar_sem_codigo_solicitado():
    resultado = validar_codigo("nenhum@email.com", "123456")
    assert resultado == "sem_codigo"

# atividade 7

from atividade_sete import calcular_media
import pytest

def test_media_normal():
    resultado = calcular_media(7, 8, 6, 9)
    assert resultado == 7.5

def test_media_maxima():
    resultado = calcular_media(10, 10, 10, 10)
    assert resultado == 10.0

def test_media_minima():
    resultado = calcular_media(0, 0, 0, 0)
    assert resultado == 0.0

def test_nota_invalida():
    resultado = calcular_media(12, 8, 6, 7)
    assert resultado == None

def test_sem_notas():
    resultado = calcular_media(None, None, None, None)
    assert resultado == None

def test_media_duas_notas():
    resultado = calcular_media(10, 5, None, None)
    assert resultado == 7.5

# atividade 8

from atividade_oito import entrada_produto, saida_produto, resetar_estoque
import pytest

def test_entrada_estoque():
    resetar_estoque()
    resultado = entrada_produto("Papel", 100)
    assert resultado == 100

def test_saida_valida():
    resetar_estoque()
    entrada_produto("Papel", 100)
    resultado = saida_produto("Papel", 30)
    assert resultado == 70

def test_saida_invalida():
    resetar_estoque()
    entrada_produto("Papel", 10)
    resultado = saida_produto("Papel", 20)
    assert resultado == False

def test_estoque_zerado():
    resetar_estoque()
    entrada_produto("Caneta", 5)
    saida_produto("Caneta", 5)
    resultado = saida_produto("Caneta", 1)
    assert resultado == False

def test_multiplas_entradas():
    resetar_estoque()
    entrada_produto("Papel", 50)
    resultado = entrada_produto("Papel", 50)
    assert resultado == 100

# atividade 9

from atividade_nove import transferir
import pytest

def test_transferencia_ok():
    resultado, saldo_a, saldo_b = transferir(1000, 0, 300)
    assert resultado == "ok"
    assert saldo_a == 700
    assert saldo_b == 300

def test_saldo_insuficiente():
    resultado, saldo_a, saldo_b = transferir(100, 0, 500)
    assert resultado == "saldo_insuficiente"

def test_valor_negativo():
    resultado, saldo_a, saldo_b = transferir(1000, 0, -100)
    assert resultado == "valor_negativo"

def test_valor_zero():
    resultado, saldo_a, saldo_b = transferir(1000, 0, 0)
    assert resultado == "valor_zero"

def test_mesma_conta():
    resultado, saldo_a, saldo_b = transferir(1000, 1000, 100, mesma_conta=True)
    assert resultado == "mesma_conta"

# atividade 10

from atividade_dez import cadastrar_turma, matricular_aluno, resetar_turmas
import pytest

def test_matricula_ok():
    resetar_turmas()
    cadastrar_turma("TI", "T1", 2)
    resultado = matricular_aluno("aluno1", "TI", "T1")
    assert resultado == "ok"

def test_turma_lotada():
    resetar_turmas()
    cadastrar_turma("TI", "T1", 0)
    resultado = matricular_aluno("aluno1", "TI", "T1")
    assert resultado == "lotada"

def test_turma_inexistente():
    resetar_turmas()
    resultado = matricular_aluno("aluno1", "TI", "T99")
    assert resultado == "nao_encontrada"

def test_turma_lota_apos_preencher():
    resetar_turmas()
    cadastrar_turma("TI", "T1", 1)
    matricular_aluno("aluno1", "TI", "T1")
    resultado = matricular_aluno("aluno2", "TI", "T1")
    assert resultado == "lotada"

def test_multiplos_alunos():
    resetar_turmas()
    cadastrar_turma("TI", "T1", 3)
    matricular_aluno("aluno1", "TI", "T1")
    resultado = matricular_aluno("aluno2", "TI", "T1")
    assert resultado == "ok"
