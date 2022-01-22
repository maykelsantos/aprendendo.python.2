from datetime import date
from time import sleep

anonascimento = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - anonascimento

print ('***DEFININDO CATEGORIA***')
sleep (2)

if idade > 0 and idade <= 9:
    print ('Você tem {} anos, então sua categoria é MIRIM!'.format(idade))
elif idade > 9 and idade <= 14:
    print ('Você tem {} anos, então sua catergoria é INFANTIL!'.format(idade))
elif idade > 14 and idade <= 19:
    print ('Você tem {} anos, então sua categoria é JÚNIOR!'.format(idade))
elif idade > 19 and idade <= 25:
    print ('Você tem {} anos, então sua categoria é SÊNIOR!'.format(idade))
elif idade > 25:
    print ('Você tem {} anos, então sua categoria é MASTER!'.format(idade))

print ('***OBRIGADO POR PARTICIPAR***')
