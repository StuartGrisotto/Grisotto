# Pedindo ao usuário o número de linhas e colunas
linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))

# Inicializamos a matriz como uma lista vazia
matriz = []

# Preenchendo a matriz com valores fornecidos pelo usuário
for i in range(linhas):  # For para cada linha
    linha = []  # Nova lista para a linha
    for j in range(colunas):  # For para cada coluna

        # Pedimos ao usuário um valor para a posição específica
        valor = int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        linha.append(valor)  # Adiciona o valor à linha
        matriz.append(linha)  # Adiciona a linha à matriz

# Exibindo a matriz resultante
print("Matriz resultante:")
for linha in matriz:
    print(linha)  # Imprime cada linha da matriz
