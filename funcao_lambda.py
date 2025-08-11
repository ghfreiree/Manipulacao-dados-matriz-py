'''
- Calculadora simples da média ponderada de notas para um estudante.
- Entrada das 3 notas (N1, N2, N3) do estudante.
- Utiliza uma função lambda para calcular a média ponderada.
- Exibe a média ponderada deste estudante. Os pesos das notas já são predefinidos, respectivamente 2, 3, 5.
'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

media_ponderada = lambda x, y, z: (x*2 + y*3 + z*5)/10
media = media_ponderada (n1, n2, n3)

print(media)