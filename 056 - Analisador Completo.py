somaidade = 0
maioridadehomem = 0
nomedohomemvelho = ''
totalmulher20 = 0

for p in range (1, 5):
    nome = str (input ('NOME: ')).strip()
    idade = int (input ('IDADE: '))
    sexo = str (input ('SEXO [M/F]: ')).strip()
    
    somaidade = somaidade + idade
    
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomedohomemvelho = nome
    
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedohomemvelho = nome
    
    if sexo in 'Ff' and idade < 20:
        totalmulher20 = totalmulher20 + 1
            
    mediaidade = somaidade / p
    
print ('A média de idade de todas essas pessoas é {}'.format(mediaidade))
print ('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomedohomemvelho))
print ('Ao todos são {} mulheres menos de 20 anos'.format(totalmulher20))
