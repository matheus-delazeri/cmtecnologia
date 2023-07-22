"""
Questão 2: implemente uma função que, dado uma matriz A e uma submatriz B
(dimensões menores que A), esta função retorne quantas vezes esta submatriz B
pode ser encontrada na matriz A.
"""

def get_matches_count(search: list, haystack: list) -> int:
    """
    Retorna o numero de ocorrências da matriz 'search' na matriz 'haystack'
    
    Parameters:
        search (list): A matriz que será buscada dentro de outra;
        haystack (list): A matriz onde a busca será performada
    """
    if not len(search) or not len(haystack):
        raise ValueError("Matrix size can't be 0")

    if type(search[0]) is not list or type(haystack[0]) is not list:
        raise ValueError("Matrix must have 2 dimensions")


    # Evita olhar linhas desnecessárias, que são menores que as dimensões da matriz 'search'
    max_row = len(haystack) - len(search) + 1
    max_col = len(haystack[0]) - len(search[0]) + 1
    count = 0
    for i in range(max_row):
        for j in range(max_col):
            if haystack[i][j] == search[0][0]:
                is_match = True
                for m in range(len(search)):
                    for n in range(len(search[0])):
                        if search[m][n] != haystack[i+m][j+n]:
                            is_match = False
                            break
                if is_match:
                    count += 1

    return count;

    

# Utilizada apenas para exibir a matriz de forma legível no terminal
def print_matrix(matrix): 
    print("\n")
    for i in range(len(matrix)):
        print(f"{matrix[i]}")
    print("\n")

matrix_a = [list(range(1, 5)) for i in range(10)]
matrix_b = [list(range(1, 3)) for i in range(5)]

print("Matriz 'haystack'")
print_matrix(matrix_a)
print("Matriz 'search'")
print_matrix(matrix_b)

matches = get_matches_count(matrix_b, matrix_a)
print(f"Número de ocorrências: {matches}")
