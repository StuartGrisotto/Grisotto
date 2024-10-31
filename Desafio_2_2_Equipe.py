
# Desafio 2.2 Equipe

# Integrantes: 
# - Stuart Grisotto
# - Leandro Alcântara Morais
# - Raylson Feitosa Alve
# - Lucas Junior Bezerra Ribeiro
# - Paulo Nunes




#Criando lista competidores
competidores = []

# Função para calcular a pontuação final descartando a maior e menor nota
#Aqui eu quebrei a cabeça, ta?
def calcular_pontuacao_final(notas):
    notas_ordenadas = sorted(notas)
    
    # Descarta a maior e a menor nota apenas se houver mais de duas notas
    if len(notas_ordenadas) > 2:
        notas_finais = notas_ordenadas[1:-1]
    else:
        notas_finais = notas_ordenadas  # Se houver duas ou menos notas ele vai usar todas
    
    return round(sum(notas_finais) / len(notas_finais), 2) if len(notas_finais) > 0 else 0





# Solicita quantidade de competidores
qtd_competidores = int(input("Digite a quantidade de competidores: "))

#INiciando For
for i in range(qtd_competidores):
    # Cadastro do nome do competidor
    nome = input(f"\nDigite o nome do {i+1}º competidor(a): ")
    qtd_manobras = int(input(f"Digite a quantidade de manobras de {nome}: "))



    # Lista de manobras para cada competidor
    manobras = []
    for j in range(qtd_manobras):
        manobra_nome = input(f"Digite o nome da {j+1}ª manobra de {nome}: ")


        notas = []  #Criando lista para armazenar as notas dos juízes
        #Coletando de notas dos juízes
        for k in range(2): #Quantidad de Juizes
            nota = float(input(f"Digite a nota do Juiz {k+1} para a manobra '{manobra_nome}': "))
            notas.append(nota)
        

        # Calcula a pontuação final da manobra e armazena
        pontuacao_manobra = calcular_pontuacao_final(notas)
        manobras.append((manobra_nome, pontuacao_manobra)) #COlocando varias variaveis em um [] da lista

    #Calculo da pontuação final do atleta
    pontuacao_final_atleta = round(sum([pontuacao for _, pontuacao in manobras]) / qtd_manobras, 2) if qtd_manobras > 0 else 0

    
    #Armazena os dados do competidor na lista principal
    competidores.append({"nome": nome, "manobras": manobras, "pontuacao_final": pontuacao_final_atleta})


# Ordena os competidores pelo ranking (pontuação final) de forma decrescente
competidores.sort(key=lambda competidor: competidor["pontuacao_final"], reverse=True)




# Exibição do ranking geral
#Eu uso o \t pra dar um espaçõ de um TAB entre as palavras. \t = TAB
print("\n===== Ranking de Competidores =====")
print("Posição\tAtleta\t\tPontuação Final")

for posicao, competidor in enumerate(competidores, start=1):
    print(f"{posicao}\t{competidor['nome']}\t\t{competidor['pontuacao_final']}")

# Exibe detalhes de cada manobra de todos os competidores

print("\n===== Detalhes das Manobras =====")
for competidor in competidores:
    print(f"\nAtleta: {competidor['nome']}")
    for manobra_nome, pontuacao in competidor["manobras"]:
        print(f"Manobra: {manobra_nome} - Pontuação: {pontuacao}\n")
