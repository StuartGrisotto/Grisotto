print("BEM VINDO A PIZZARIA PYTHON!!")

while True:
    tamanho = int(input("Escolha o tamanho da Pizza:\n\n1 - pequeno\n2 - Médio\n3 - Grande\n\n"))
    sabore = int(input("Escolha os sabores:\n\n1 - Calabreza\n2 - Frango\n3 - Marguerita\n4 - Quatro Queijos\n\n"))

    print("Dados do Pedido:")
    if tamanho == 1:
        print("Tamanho da pizza Pequena")
    if tamanho == 2:
        print("Tamanho da pizza Média")
    if tamanho == 3:
        print("Tamanho da pizza Grande")
    
    if sabore == 1:
        print("Sabor de Calabreza")
    if sabore == 2:
        print("Sabor de Frango")
    if sabore == 3:
        print("Sabor de Marguerita")
    if sabore == 4:
        print("Sabor de Quatro Queijos")

    continuar = str(input("Deseja adicionar mais uma pizza? (S/N): \n"))
    if continuar != 'S':
        break
        
    
        
    
         