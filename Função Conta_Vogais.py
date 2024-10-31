def contador_de_vogais (texto):
    vogais  = 'a,e,i,o,u,A,E,I,O,U'
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador +=1
    
    return contador

resultado = contador_de_vogais(str(input('Digite um texto: ')))
print(f'O numero de vogais é:  {resultado}')