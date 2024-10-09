print('Desafio 2.1')
a = int(input('Digite o seu primeiro número: '))
b = int(input('Digite o seu segundo número: '))
c = int(input('Digite o seu terceiro número: '))

if a > b and a > c and b > c:
    print(f'A ordem decrescente é {a} , {b} e {c}')
if a > b and a > c and c > b:
    print(f'A ordem decrescente é {a} , {c} e {b}')
    
if b > a and b > c and c > a:
    print(f'A ordem decrescente é {b} , {c} e {a}')
if b > a and b > c and a > c:
    print(f'A ordem decrescente é {b} , {a} e {c}')
    
if c > a and c > b and a > b:
    print(f'A ordem decrescente é {c} , {a} e {b}')
if c > a and c > b and b > a:
    print(f'A ordem decrescente é {c} , {b} e {a}')