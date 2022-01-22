#Esse código ainda está em aprendizado!

pt = int (input ('Informe o Primeiro Termo: '))
r = int (input ('Informe a Razão: '))
dec = (pt + 9) * r

for c in range (pt, dec, r):
    print ('{} ->'.format (c))
