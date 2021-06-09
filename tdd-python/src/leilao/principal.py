from src.leilao.dominio import Leilao, Usuario, Lance


user_1 = Usuario('Fi')
user_2 = Usuario('Fu')


lance_1 = Lance(user_1, 100.0)
lance_2 = Lance(user_2, 200.0)



leilao = Leilao('Civic')
leilao.lances.append(lance_1)
leilao.lances.append(lance_2)

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'Maior lance: {avaliador.maior_lance}')
print(f'Menor lance: {avaliador.menor_lance}')