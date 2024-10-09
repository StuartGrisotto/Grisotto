# Definição dos fatores de multiplicação para cada tamanho de pizza
tamanhos = {
    'Pequena': 1.0,
    'Média': 1.2,
    'Grande': 1.5
}

# Definição dos preços base para cada sabor de pizza
sabores = {
    'Calabresa': 10.0,
    'Marguerita': 12.0,
    'Quatro queijos': 15.0,
    'Frango': 14.0
}

# Inicialização de variáveis
total_pedido = 0.0
continuar_pedido = 'S'

while continuar_pedido.upper() == 'S':
    quantidade_pizzas = int(input("Quantas pizzas você gostaria de pedir? "))
    
    for i in range(quantidade_pizzas):
        print(f"\nPedido da pizza {i + 1}:")
        
        # Escolha do tamanho da pizza
        print("Escolha o tamanho da pizza:")
        for tamanho in tamanhos:
            print(f"- {tamanho}")
        tamanho_escolhido = input("Digite o tamanho desejado: ")
        while tamanho_escolhido not in tamanhos:
            print("Tamanho inválido. Por favor, escolha entre Pequena, Média ou Grande.")
            tamanho_escolhido = input("Digite o tamanho desejado: ")
        fator_tamanho = tamanhos[tamanho_escolhido]

        # Escolha dos sabores
        print("Escolha até dois sabores:")
        for sabor in sabores:
            print(f"- {sabor}")
        sabor1 = input("Digite o primeiro sabor: ")
        while sabor1 not in sabores:
            print("Sabor inválido. Por favor, escolha entre Calabresa, Marguerita, Quatro queijos ou Frango.")
            sabor1 = input("Digite o primeiro sabor: ")
        sabor2 = input("Digite o segundo sabor (ou pressione Enter para nenhum): ")
        if sabor2 and sabor2 not in sabores:
            print("Sabor inválido. O segundo sabor será ignorado.")
            sabor2 = None

        # Cálculo do preço da pizza
        preco_base = sabores[sabor1]
        if sabor2:
            preco_base += sabores[sabor2]
        preco_pizza = preco_base * fator_tamanho

        # Adição ao total do pedido
        total_pedido += preco_pizza
        print(f"Pizza {i + 1} adicionada ao pedido! Valor: R$ {preco_pizza:.2f}")
    
    # Pergunta sobre continuar o pedido
    continuar_pedido = input("\nGostaria de fazer mais um pedido (S - Sim ou N - Não)? ")

# Exibição do valor total do pedido
print(f"\nO valor total do seu pedido é: R$ {total_pedido:.2f}")
