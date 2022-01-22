from time import sleep

v = (0)

n = int(input('Informe um número inteiro: '))
print ('A tabuada do número {} será listada abaixo.'.format(n))

for c in range (0, 10):
    v = (v + 1)
    print ('{} X {} = {}'.format(n, v, (n * v)))
    sleep (0.5)
