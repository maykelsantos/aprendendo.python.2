s = 0

for contador in range (0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s = s + n
        
print ('A soma dos números pares é {}'.format(s))
