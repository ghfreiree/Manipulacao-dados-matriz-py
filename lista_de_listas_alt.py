'''
- Organiza uma matriz de notas e nomes a partir de uma lista comum
- Cada sublista contém o nome do aluno e suas respectivas notas
- Exibe a lista de listas organizadas
'''

notas_e_nomes = ['João', 6.5, 8.9, 4.7, 'Maria', 8.9, 9.1, 7.9, 'José', 3.4, 5.6, 2.4, 'Pedro', 6.7, 7.5, 8.2, 'Enzo', 2.5, 7.8, 5.6]

notas_lista_org = []

for i in range(0, len(notas_e_nomes), 4):
    notas_lista_org.append([notas_e_nomes[i], notas_e_nomes[i+1], notas_e_nomes[i+2], notas_e_nomes[i+3]])

print(notas_lista_org)