#Declarando as variaveis com valor inicial de 0
tot_debito = 0
tot_credito = 0

#Usuario atribui valor inicial para a receita
vlr_receita = int(input("Digite o valor inicial da receita\n"))

#Inicio do WhileTrue
while True:

    #Usuario escolhe a ação de credito ou debito
    acao = str(input("Escolha a ação \n (D - Debito / C - Credito)\n"))
    
    #Caso o usuario escolha Credito, O valor será somado a receita e ao valor total de credito
    if acao == "C" :
        vlr_crd = float(input("Digite o valor do Credito \n"))
        vlr_receita += vlr_crd
        tot_credito +=vlr_crd
        
    #Caso o usuario escolha Debito, O valor será subitraido a receita e somado ao valor total de Debito
    if acao == "D" :
        vlr_dbt = float(input("Digite o valor do Debito \n"))
        vlr_receita -= vlr_dbt
        tot_debito += vlr_dbt

    #Condição para continuar dentro do while
    continuar = str(input("Deseja adicionar mais alguma ação? (S/N): \n"))
    if continuar != 'S':
        break
    
#Informando os dados para o usuario
print("\n\nValor total da receita: ", vlr_receita)
print("Valor total de Debito: ", tot_debito)
print("Valor total de credito" , tot_credito)