'''
- Separa os nomes dos alunos de suas notas através de um laço de repetição e uma estrutura condicional
- Organiza as notas de cada aluno em listas diferentes dentro de uma matriz
- Exibe a matriz
'''

notas_e_nomes = ['João', 6.5, 8.9, 4.7, 'Maria', 8.9, 9.1, 7.9, 'José', 3.4, 5.6, 2.4, 'Pedro', 6.7, 7.5, 8.2, 'Enzo', 2.5, 7.8, 5.6]

nomes = []
notas = []

for i in range(len(notas_e_nomes)):
    if i%4 == 0:
        nomes.append(notas_e_nomes[i])
    else:
        notas.append(notas_e_nomes[i])

notas_listas = []

for y in range(0, len(notas), 3):
    notas_listas.append([notas[y], notas[y+1], notas[y+2]])

print(f'{notas_listas}')