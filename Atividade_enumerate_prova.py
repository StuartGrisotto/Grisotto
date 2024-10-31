nomes = [] #Indica que a variavel nome é uma lista/Vetor
for i in range (5): #Iniciando um for de 5 espaços
    nome = input(f'Digite o nome {i+1}:') #Perguntando o nome com contador i
    nomes.append(nome) #Guardando a variavem nome em append\lista
    print('\nOs nomes inseridos foram: ')
    for i, nome in enumerate(nomes, start=1): #Criando numeração na varial nome conforme os dados entram
        print(f"{i} - {nome}")#Mostrando o contador com o a variavel nome