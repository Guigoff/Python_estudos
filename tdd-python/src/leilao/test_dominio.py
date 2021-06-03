import sys
from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        user_1 = Usuario('Fi')
        user_2 = Usuario('Fu')

        lance_1 = Lance(user_1, 100.0)
        lance_2 = Lance(user_2, 200.0)

        leilao = Leilao('Carro')
        leilao.lances.append(lance_1)
        leilao.lances.append(lance_2)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)