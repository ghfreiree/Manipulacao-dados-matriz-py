'''
- Calcula a média de notas de alunos a partir de uma matriz
- Cada linha da matriz contém três notas de um aluno
- Utiliza o list comprehension para calcular a média de cada linha da matriz
- Exibe a média de cada aluno
'''

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def calc_media(x) -> float:
	'''
	- Realiza o cálculo da média de uma lista de números
	- Retorna a média
	'''
	media = sum(x)/len(x)
	return media

media = [calc_media(trio_notas) for trio_notas in notas]

print(media)