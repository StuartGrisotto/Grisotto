def encontrar_repetidos(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    repetidos = conjunto1.intersection(conjunto2)
    return list(repetidos)

print("\nFunção de Elementos Comuns\n")

list1 = input("Digite a Lista 1 de números separados por espaço: ").split()
list2 = input("Digite a Lista 2 de números separados por espaço: ").split()

# Verifica se todos os itens na lista são números inteiros
digitou_so_numero = True
try:
    nums1 = list(map(int, list1))
    nums2 = list(map(int, list2))
except ValueError:
    digitou_so_numero = False

if digitou_so_numero:
    repetidos = encontrar_repetidos(nums1, nums2)
    print(f"Elementos comuns às duas listas: {repetidos}")
else:
    print("Entrada inválida.")
