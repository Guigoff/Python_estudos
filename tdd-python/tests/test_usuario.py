from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture()
def danilo():
    return Usuario('Danilo', 200.0)


@pytest.fixture()
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(danilo, leilao):
    danilo.propoe_lance(leilao, 100.0)
    assert danilo.carteira == 100.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(danilo, leilao):
    danilo.propoe_lance(leilao, 1.0)
    assert danilo.carteira == 199.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(danilo, leilao):
    danilo.propoe_lance(leilao, 200.0)
    assert danilo.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(danilo, leilao):
    with pytest.raises(LanceInvalido):
        danilo.propoe_lance(leilao, 201.0)
