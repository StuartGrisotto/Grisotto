lista1 = []
lista2 = []

for i in range(5):
    set1 = input(f"Digite um o {i+1}º numero, Lista1: ")
    lista1.append(set1)
    set2 = input(f"Digite um o {i+1}º numero, Lista2: ")
    lista2.append(set2)
    




# Leitura das listas

lista1 = input().split()

lista2 = input().split()



# Verifica se todas os elementos das listas podem ser convertidos para inteiros

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):

    comuns = elementos_comuns(lista1, lista2)

    print(f"Elementos comuns às duas listas: {comuns}")

else:

    print("Entrada inválida.")


return list(set1.intersection(set2))