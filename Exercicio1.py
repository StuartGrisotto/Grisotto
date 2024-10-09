#Declarando as variaveis com valor inicial de 0
ccp_menos_23 = 0
ads_like = 0
tot_alunos = 0

#Inicio do WhileTrue
while True:
    #Atribundo as informações digitadas nas respectivas variaveis
    curso = str(input("Digite o curso (CCP / ADS): "))
    age = int(input("Digite a idade: "))
    gosta = str(input("Gosta do curso? (S / N): "))
    #Somando mais 1 aluno em total de alunos que respoderam as atividades
    tot_alunos += 1
    
    #Condição de atribuir Alunos CCP menores de 23 anos
    if curso == 'CCP' and age < 23:
        ccp_menos_23 += 1
    #Condição de atribuir Alunos que gostam do curso ADS
    if curso == 'ADS' and gosta == 'S':
        ads_like += 1

    #Condição para continuar dentro do while
    continuar = str(input("Deseja adicionar mais um aluno? (S/N): "))
    if continuar != 'S':
        break

#Informando os dados para o usuario
print("\n\nTotal de alunos entrevistados:", tot_alunos)
print("Número de alunos de CCP com menos de 23 anos: ",ccp_menos_23)
print("Número de alunos de ADS que estão gostando do curso:", ads_like)
