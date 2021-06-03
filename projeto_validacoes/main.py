import requests

from documento import Documento
from telefone import Telefone
from datas import Cadastro
from cep import Cep

##TESTES DE DOCUMENTO
#
# cpf = Documento.criar_documento('')
# cnpj = Documento.criar_documento('')
#
# print(cnpj)
# print(cpf)
#


##TESTES TELEFONE
##Necessário passar o DDD com ()
# numero = ''
#
# obj = Telefone(numero)
# print(obj)


##TESTE DATA
#
# cadastro = Cadastro()
# print(cadastro.tempo_cadastro())
# print(cadastro)

##TESTE CEP
cep = Cep('01001000')
cep.retorna_endereco()
bairro, cidade, estado = cep.retorna_endereco()
print(bairro)
print(cidade)
print(estado)

