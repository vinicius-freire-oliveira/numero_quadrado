# Lista de inteiros
inteiros = [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ,17 ,18 ,19, 20]

# Lista de quadrados usando uma list comprehension
# Cada elemento 'n' da lista 'inteiros' é elevado ao quadrado e colocado na lista 'quadrados'
quadrados = [n * n for n in inteiros]

# Imprime a lista 'quadrados' contendo os quadrados dos números da lista 'inteiros'
print(quadrados)
