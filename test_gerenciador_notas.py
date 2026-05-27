import pytest
from gerenciador_notas import GerenciadorNotas


class TestCadastrarNota:

    def test_cadastrar_nota_valida(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(8.0)
        assert 8.0 in g.notas

    def test_cadastrar_nota_zero(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(0)
        assert 0 in g.notas

    def test_cadastrar_nota_dez(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(10)
        assert 10 in g.notas

    def test_cadastrar_nota_invalida_acima(self):
        g = GerenciadorNotas()
        with pytest.raises(ValueError):
            g.cadastrar_nota(11)

    def test_cadastrar_nota_invalida_negativa(self):
        g = GerenciadorNotas()
        with pytest.raises(ValueError):
            g.cadastrar_nota(-1)


class TestCalcularMedia:

    def test_media_correta(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(6.0)
        g.cadastrar_nota(8.0)
        assert g.calcular_media() == 7.0

    def test_media_sem_notas(self):
        g = GerenciadorNotas()
        assert g.calcular_media() == 0.0

    def test_media_uma_nota(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(9.0)
        assert g.calcular_media() == 9.0


class TestVerificarSituacao:

    def test_situacao_aprovado(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(7.0)
        g.cadastrar_nota(8.0)
        assert g.verificar_situacao() == "Aprovado"

    def test_situacao_recuperacao(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(5.0)
        g.cadastrar_nota(6.0)
        assert g.verificar_situacao() == "Recuperação"

    def test_situacao_reprovado(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(3.0)
        g.cadastrar_nota(4.0)
        assert g.verificar_situacao() == "Reprovado"

    def test_situacao_media_exatamente_7(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(7.0)
        assert g.verificar_situacao() == "Aprovado"

    def test_situacao_media_exatamente_5(self):
        g = GerenciadorNotas()
        g.cadastrar_nota(5.0)
        assert g.verificar_situacao() == "Recuperação"