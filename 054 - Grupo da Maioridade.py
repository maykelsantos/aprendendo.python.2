from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for pessoa in range (1, 8):
    nasc = int (input ('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc

    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
    
print ('Ao todo tivemos {} pessoas maiores de idade e {} pessoas menore de idade!'.format(totalmaior, totalmenor))
