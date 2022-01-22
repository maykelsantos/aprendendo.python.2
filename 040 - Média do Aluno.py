from time import sleep
nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
media = (nota1 + nota2) / 2
print ('***CALCULANDO SUA MÉDIA***')
sleep (2)
if media < 5:
    print ('''***REPROVADO***
Média: {:.1f}'''.format(media))
elif media > 5 and media < 7:
    print ('''***RECUPERAÇÃO***
Média: {:.1f}'''.format(media))
else:
    print ('''***APROVADO***
Média: {:.1f}'''.format(media))
