url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

##Parâmetros
index_interrogation = url.find('?')
url_base = url[:index_interrogation]
url_parameters = url[index_interrogation+1:]

##Parâmetros de busca
search_parameters = 'moedaOrigem'
index_parameters = url_parameters.find(search_parameters)
index_value = index_parameters + len(search_parameters) + 1
index_separator = url_parameters.find('&', index_parameters)
if index_separator == -1:
    value = url_parameters[index_value:]
else:
    value = url_parameters[index_value:index_separator]

print(value)