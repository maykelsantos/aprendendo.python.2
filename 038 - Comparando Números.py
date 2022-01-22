num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro núemro inteiro: '))
if num1 > num2:
    print ('''O número maior é {}
O número menor é {}'''.format(num1, num2))
elif num1 < num2:
    print ('''O número maior é {}
O número menor é {}'''.format(num2, num1))
else:
    print('Não exite número maior, ambos são iguais!')
