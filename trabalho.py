disciplinas = int(input('Quantas disciplinas da UACSA você já cursou? '))

if disciplinas < 0:
    print('Esse valor é INVÁLIDO')
if disciplinas >= 0 and disciplinas <= 7:
    print('Você é CALOURO(A)')
if disciplinas > 7 and disciplinas <= 15:
    print('Você é SOBREVIVENTE')
if disciplinas > 15 and disciplinas <= 25:
    print('Você é FUTURO(A) ENGENHEIRO(A)')
if disciplinas > 25 and disciplinas <= 30:
    print('Você é VETERANO(A) DE GUERRA')
if disciplinas > 30:
    print('Você está QUASE LÁ')