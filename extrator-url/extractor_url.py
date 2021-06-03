import re

class ExtractorUrl:
    def __init__(self,url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def validate_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        default_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = default_url.match(self.url)

        if not match:
            raise ValueError('A URL não é valida')

    def get_url_base(self):
        index_interrogation = self.url.find('?')
        url_base = self.url[:index_interrogation]
        return url_base

    def get_url_parameter(self):
        index_interrogation = self.url.find('?')
        url_parameters = self.url[index_interrogation + 1:]
        return url_parameters

    def get_value_parameter(self, parameter):
        index_parameters = self.get_url_parameter().find(parameter)
        index_value = index_parameters + len(parameter) + 1
        index_separator = self.get_url_parameter().find('&', index_parameters)
        if index_separator == -1:
            value = self.get_url_parameter()[index_value:]
        else:
            value = self.get_url_parameter()[index_value:index_separator]

        return value

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'Parâmetros: ' + self.get_url_parameter() + '\n' + 'URL Base: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real'
extractor_url = ExtractorUrl(url)
value_dollar = 5.50
currency_o = extractor_url.get_value_parameter('moedaOrigem')
currency_d = extractor_url.get_value_parameter('moedaDestino')
qtd = float(extractor_url.get_value_parameter('quantidade'))

if currency_o == 'real' and currency_d == 'dolar':
    value_changed = int(qtd)/value_dollar
    print(f'O valor de R$ {qtd} reais é igual a $ {str(value_changed)} dólares.')
elif currency_o == 'dolar' and currency_d == 'real':
    value_changed = int(qtd) * value_dollar
    print(f'O valor de $ {qtd} dólares é igual a R$ {str(value_changed)} reais.')
else:
    print(f"Câmbio de {currency_o} para {currency_d} não está disponível.")