from time import sleep
from datetime import date
anoidade = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = (anoatual - anoidade)
print('***VERIFICANDO INFORMAÇÕES***')
sleep (2)
if idade < 18:
    print ('Você ainda vai se alistar em {} anos. Fique atento!'.format(18 - idade))
elif idade > 18:
    print ('Você já passou da hora de se alistar, fazem {} anos.'.format(idade - 18))
else:
    print ('Você está na hora exata para se alistar, parabéns!')
