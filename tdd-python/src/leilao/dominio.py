import sys

from src.leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_valido(valor):
            raise LanceInvalido('Valor do lance maior que saldo')

        leilao.propoe(Lance(self, valor))
        self.__carteira -= valor

    def _valor_valido(self, valor):
        return self.__carteira >= valor


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance: Lance):

        if self._lance_valido(lance):
            if not self._possui_lance():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor
            self.__lances.append(lance)

    def _possui_lance(self):
        return self.__lances

    def _usuario_diferente(self, lance):

        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuário não pode dar dois lances seguidos')


    def _lance_maior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance deve ser maior que o lance anterior')

    def _lance_valido(self, lance):
        return not self._possui_lance() or self._usuario_diferente(lance) and self._lance_maior(lance)
