frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print ('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print ('Temos um PALÍNDROMO!')
else:
    print ('A frase digitada NÃO É UM PALÍNDROMO!')
