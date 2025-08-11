'''
- Separa os primeiros nomes dos alunos em uma lista com o list comprehension
- Cria uma lista de tuplas com o nome do aluno e sua respectiva nota com a função zip()
- Exibe a lista de tuplas com nome e nota dos alunos
'''

lista_alunos = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]

notas = [9.0, 7.3, 5.8, 6.7, 8.5]

nomes = [tuplas[0] for tuplas in lista_alunos]

alunos = list(zip(nomes, notas))

print(alunos)