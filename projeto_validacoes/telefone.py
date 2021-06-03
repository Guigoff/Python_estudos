import re

class Telefone:


    def __init__(self, telefone):
        if self.valida(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número incorreto.')

    def __str__(self):
        return self.formata()

    def valida(self, telefone):
        padrao = '([0-9]{2,3})?(\([0-9]{2}\))([0-9]{4,5})([0-9]{4})'
        return re.findall(padrao, telefone)

    def formata (self):
        padrao = '([0-9]{2,3})?(\([0-9]{2}\))([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        return '{} {} {}-{}'.format(
            '+' + resposta.group(1) if resposta.group(1) is not None else ''
            , resposta.group(2)
            , resposta.group(3)
            , resposta.group(4)
        )
