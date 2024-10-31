# STUART GRISOTTO
# RGM: 40195376
# grisotto.work@gmail.com

# NF = 0.4 * N1 + 0.6 * N2

#criando lista "dados"
dados = []

#Perguntando quantos alunos para inicar o "FOR"
qtd_aluno = int(input("Digite a quantidade de alunos: "))

# For para armazenar quantos dados o usuario cololar em qtidade de alunos
for i in range(qtd_aluno):
    aluno = input(f"Digite o nome do {i+1}º aluno: ")
    n1 = float(input("Digite a Nota 1 deste aluno: "))
    n2 = float(input("Digite a Nota 2 deste aluno: "))
    NF = 0.4 * n1 + 0.6 * n2  # Calcula a nota final para o aluno
    
    # Armazena os dados de cada aluno em uma lista
    dados.append((aluno, n1, n2, NF))

# Imprime a tabela de alunos com as notas e a nota final
print("\nNúmero\tNome\tNota1\tNota2\tNota Final")
for i, (aluno, n1, n2, NF) in enumerate(dados, start=1):
    print(f"{i}\t{aluno}\t{n1}\t{n2}\t{NF:.2f}")
