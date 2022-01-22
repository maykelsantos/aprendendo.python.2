from random import choice
from time import sleep

jogador = int(input('''Escolha um dos itens abaixo:
                    
        [1] PEDRA
        [2] PAPEL
        [3] TESOURA
                    
Minha escolha é: '''))

print ('[...] REGISTRANDO SUA ESCOLHA [...]')

sleep (2)

escolha = [1, 2, 3]

computador = choice(escolha)

if jogador != 1 and jogador != 2 and jogador != 3:
    print ('[...] ESCOLHA INVÁLIDA [...]')

if jogador == computador:
    print ('Eu escolhi a mesma que você, empatamos!')
elif jogador == 1 and computador == 2:
    print ('Eu escolhi PAPEL e ganhei, tente novamente!')
elif jogador == 1 and computador == 3:
    print ('Eu escolhi TESOURA. Você ganhou, parabéns!')
elif jogador == 2 and computador == 1:
    print ('Eu escolhi PEDRA. Você ganhou, parabéns!')
elif jogador == 2 and computador == 3:
    print ('Eu escolhi TESOURA e ganhei, tente novamente!')
elif jogador == 3 and computador == 1:
    print ('Eu escolhi PEDRA e ganhei, tente novamente!')
elif jogador == 3 and computador == 2:
    print ('Eu escolhi PAPEL. Você ganhou, parabéns!')
