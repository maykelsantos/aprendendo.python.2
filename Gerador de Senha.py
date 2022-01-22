import random

min = 'abcdefghijklmnopqrstuvxzwy'
mai = 'ABCDEFGHIJKLMNOPQRSTUVXZWY'
num = '0123456789'
sim = '[]{(})*;/,._-#@%$!&+°ºª:><\|'

all = min + mai + num + sim

total = 16

senha = ''.join(random.sample(all, total))

print (senha)
