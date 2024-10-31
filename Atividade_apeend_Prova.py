nomes = [] #Indica que a variavel nome é uma lista/Vetor
for i in range (5): #Iniciando um for de 5 espaços
    nome = input(f'Digite o nome {i+1}:') #Perguntando o nome com contador i
    nomes.append(nome) #Guardando\add a variavem nome em append\lista
    print('\nOs nomes inseridos foram: ')
    for nome in nomes: #Usando o for para mostrar todos os nomes
        print(nome.title()) #Mostrando os nomes dentro do for