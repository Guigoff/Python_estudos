import requests

class Cep:

    def __init__(self, cep):
        cep = str(cep)
        if len(cep) == 8:
            self.cep = cep
        else:
            raise ValueError('Quantidade de digitos inválidos para CEP')

    def __str__(self):
        return self.formata_cep()

    def formata_cep(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def retorna_endereco(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        r = requests.get(url).json()
        return r['bairro'], r['localidade'], r['uf']


