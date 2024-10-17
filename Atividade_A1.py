# STUART GRISOTTO
# RGM: 40195376
# grisotto.work@gmail.com


dados = [] # Inicializa uma lista vazia para armazenar os dados do currículo
while True:  # Inicia um loop WHILE
    print("## Cadastro de Curriculo ##")  # Título do formulário de cadastro

    # Solicita o nome do candidato e adiciona à lista 'dados'
    nome = input(f'Digite o Nome: ')
    dados.append(nome)

    # Solicita o CPF e adiciona à lista 'dados'
    cpf = input(f'Digite o CPF: ')
    dados.append(cpf)

    # Solicita o telefone e adiciona à lista 'dados'
    tel = input('Digite o seu Telefone: ')
    dados.append(tel)

    # Solicita o estado civil do candidato, com opções numeradas
    estado_civil = input('Informe o seu Estado Civil\n1 - Solteiro\n2 - Casado\n3 - Separado\n4 - Divorciado\n5 - Viúvo\n')

    # Verifica a entrada do usuário e atribui uma descrição correspondente ao estado civil
    if estado_civil == '1':
        estado_civil_desc = 'Solteiro'
    elif estado_civil == '2':
        estado_civil_desc = 'Casado'
    elif estado_civil == '3':
        estado_civil_desc = 'Separado'
    elif estado_civil == '4':
        estado_civil_desc = 'Divorciado'
    elif estado_civil == '5':
        estado_civil_desc = 'Viúvo'
    else:
        estado_civil_desc = 'Estado Civil Inválido'

    # Adiciona a descriç~ao do estado civil à lista 'dados'
    dados.append(estado_civil_desc)

    # Solicita o endereço e o adiciona à lista dados
    end = input('Digite seu Endereço: ')
    dados.append(end)

    # Solicita o email e adiciona à lista dados
    email = input('Digite o seu Email: ')
    dados.append(email)

    # Solicita uma breve descrição e adiciona à lista dados
    curriculo = input('Digite um curta descrição (Minicurriculo):\n')
    dados.append(curriculo)


    # print('\nDados curriculo:')
    # for dado in dados:
    #     print(dado)


    # Pergunta ao usuário se deseja cadastrar um novo currículo
    continuar = input("Deseja Cadastrar novamente? (S/N): \n").strip().upper()
    
    # Se a resposta não for 'S' o loop é encerrado.
    if continuar != 'S':
        break

# Exibindo os dados formatando de forma organizada.
print("\n## CURRÍCULO FINALIZADO ##\n")
print("Candidato: {}\tCPF: {}".format(dados[0], dados[1]))  # Exibe nome e CPF
print("Contato: {}\tEstado Civil: {}".format(dados[2], dados[3]))  # Exibe telefone e estado civil
print("Endereço: {}\tE-mail: {}".format(dados[4], dados[5]))  # Exibe endereço e email
print("\nDescrição Pessoal:\n{}".format(dados[6]))  # Exibe a breve descrição pessoal
