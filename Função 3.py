#Função - Definida pelo usuario

#Criando função
def cadastro():
    nome=[] # Criando Lista
    for i in range(5): #Criando for até range de 5
        nomecad = input(f'Digite o nome {i+1}: ')
        nome.append(nomecad) #Salvando o nome da lista
        print(nome) # Mostrar nome depois de inserido

#Chamando a função
cadastro()