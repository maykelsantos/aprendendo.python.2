pesado = 0
leve = 0

for pessoa in range (1, 6):
    peso = float (input ('Informe o peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso

print ('O maior peso lido foi {}Kg'.format(pesado))
print ('O menor peso lido foi {}Kg'.format(leve))