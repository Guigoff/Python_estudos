class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formada(self):
        print('{:02d}/{:02d}/{}'.format(self.dia, self.mes, self.ano))
