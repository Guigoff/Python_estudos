from datetime import datetime, timedelta

class Cadastro:

    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def tempo_cadastro(self):
        #TESTE PARA ADICIONAR DIAS
        # agora = datetime.today() + timedelta(days=15, minutes=20, seconds=30)

        agora = datetime.today()
        return agora - self.data_cadastro

    def mes_cadastro(self):
        meses = {
            1 : 'Janeiro',
            2 : 'Fevereiro',
            3 : 'Março',
            4 : 'Abril',
            5 : 'Maio',
            6 : 'Junho',
            7 : 'Julho',
            8 : 'Agosto',
            9 : 'Setembro',
            10 : 'Outubro',
            11 : 'Novembro',
            12 : 'Dezembro',
        }

        mes = self.data_cadastro.month
        return meses[mes]

    def formata_data(self):
       return self.data_cadastro.strftime('%d/%m/%Y %H:%M')