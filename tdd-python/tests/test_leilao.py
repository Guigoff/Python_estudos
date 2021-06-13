from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.user_1 = Usuario('Fi', 200.0)
        self.lance_1 = Lance(self.user_1, 100.0)
        self.leilao = Leilao('Carro')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):

        user_2 = Usuario('Fu',200.0)
        lance_2 = Lance(user_2, 200.0)

        self.leilao.propoe(self.lance_1)
        self.leilao.propoe(lance_2)

        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        user_2 = Usuario('Fu',200.0)
        lance_2 = Lance(user_2, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(lance_2)
            self.leilao.propoe(self.lance_1)


    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_apenas_um_lance(self):
        self.leilao.propoe(self.lance_1)

        menor_valor_esperado = 100
        maior_valor_esperado = 100

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_tres_lances(self):
        user_2 = Usuario('Fu',200.0)
        user_3 = Usuario('Fa',200.0)
        lance_2 = Lance(user_2, 200.0)
        lance_3 = Lance(user_3, 500.0)

        self.leilao.propoe(self.lance_1)
        self.leilao.propoe(lance_2)
        self.leilao.propoe(lance_3)

        menor_valor_esperado = 100
        maior_valor_esperado = 500

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_1)

        self.assertEqual(1, len(self.leilao.lances))

    def teste_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        user_2 = Usuario('Fu',200.0)
        lance_2 = Lance(user_2, 200.0)

        self.leilao.propoe(self.lance_1)
        self.leilao.propoe(lance_2)

        self.assertEqual(2, len(self.leilao.lances))

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_1)
            self.leilao.propoe(Lance(self.user_1, 200))

    def test_nao_deve_permitir_propor_lance_caso_o_lance_seja_menor_que_o_anterior(self):
        user_2 = Usuario('Fu',200.0)
        lance_2 = Lance(user_2, 50.0)
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_1)
            self.leilao.propoe(lance_2)
