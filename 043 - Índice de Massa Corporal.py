from time import sleep

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura ** 2)

print ('*** CALCULANDO SEU IMC ***')
sleep (2)

if imc < 18.5:
    print ('Seu IMC é {:.1f}, sendo assim você está ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print ('Seu IMC é {:.1f}, sendo assim você está no PESO IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print ('Seu IMC é {:.1f}, sendo assim você está com SOBREPESO!'.format(imc))
elif imc >= 30 and imc < 40:
    print ('Seu IMC é {:.1f}, sendo assim você está em OBESIDADE!'.format(imc))
elif imc >= 40:
    print ('Seu IMC é {:.1f}, sendo assim você está em OBESIDADE MÓRBIDA!'.format(imc))
