from random import randint
'''
- Gera códigos únicos para cada aluno a partir da inicial dos seus nomes
- Cria uma lista de tuplas com o nome do aluno e seu respectivo código
- Exibe a lista de tuplas
'''

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]

def gera_codigo():
    return str(randint(0, 999))

lista_codigos = []

for i in range(len(estudantes)):
    lista_codigos.append((estudantes[i], estudantes[i][0] + gera_codigo()))

print(lista_codigos)