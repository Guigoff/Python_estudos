from validate_docbr import CPF
from validate_docbr import CNPJ


class Documento:

    @staticmethod
    def criar_documento(documento):
        documento = Documento.limpa_caracteres(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de digitos inválida!')


    def limpa_caracteres(documento):
        documento = str(documento)
        for ch in ['-', '.', '/']:
            if ch in documento:
                documento = documento.replace(ch, '')
        return documento


class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.documento = documento
        else:
            raise ValueError('CPF inválido!')

    def __str__(self):
        mask = CPF()
        return mask.mask(self.documento)

    def valida(self, documento):
        valida = CPF()
        return valida.validate(documento)


class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.documento = documento
        else:
            raise ValueError('CNPJ Inválido.')

    def __str__(self):
        mask = CNPJ()
        return mask.mask(self.documento)

    def valida(self, documento):
        cnpj = CNPJ()
        return cnpj.validate(documento)
