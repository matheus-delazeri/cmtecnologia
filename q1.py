"""
Questão 1: implemente uma função que inverta as diagonais de uma matriz
quadrada.
"""


# Número de colunas e linhas padrão da matriz
SIZE = 10

def invert(matrix):
    for i in range(len(matrix)):
        inverse_index = len(matrix) - (i+1) # Index diretamente oposto ao atual (i)
        tmp = matrix[i][i]
        matrix[i][i] = matrix[i][inverse_index]
        matrix[i][inverse_index] = tmp

    return matrix


# Utilizada apenas para exibir a matriz de forma legível no terminal
def print_matrix(matrix): 
    print("\n")
    for i in range(len(matrix)):
        print(f"{matrix[i]}")
    print("\n")

"""
 list(range(1, SIZE)) > Retorna uma lista de tamanho SIZE onde o valor de cada item é seu próprio index (+1)
 for i in range(SIZE) > Itera pela matriz e adiciona o retorno de [0]*SIZE à linha atual
"""
example_matrix = [list(range(1, SIZE+1)) for i in range(SIZE)]
print("Inicial:")
print_matrix(example_matrix)
print("Invertida: ")
print_matrix(invert(example_matrix))
