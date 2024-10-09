# Inicializando as variáveis
soma_notas = 0  # Armazena a soma de todas as notas dos alunos
contador = 1    # Controla o número de alunos inseridos, começa em 1

# Loop com WHILE para coletar as notas dos 30 alunos
while contador <= 30:
    # Solicita ao professor que insira a nota do aluno
    nota = float(input(f"Digite a nota do aluno {contador}: "))
    
    # Verifica se a nota está entre 0 e 10
    if 0 <= nota <= 10:
        # Adiciona a nota à soma das notas
        soma_notas += nota
        
        # Incrementa o contador para o próximo aluno
        contador += 1
    else:
        # Se a nota não for válida, exibe uma mensagem e repete a solicitação
        print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")

# Calcula a média aritmética das notas
media = soma_notas / 30

# Exibe a média aritmética
print(f"A média aritmética das notas dos 30 alunos é: {media:.2f}")
