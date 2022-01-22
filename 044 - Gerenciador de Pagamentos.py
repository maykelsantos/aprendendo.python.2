from time import sleep

item = int(input('''Escolha o item a ser comprado:
                    [1] CARRO R$45.000,00
                    [2] MOTO R$12.000,00
                    [3] BARCO R$92.000,00
                    
                    Item: '''))

print ('[...] RESGITRANDO ITEM [...]')
sleep (2)

if item != 1 and item != 2 and item != 3:
    print ('[...] OPÇÃO INVÁLIDA [...]')
else:
    forma = int(input('''Agora, escolha a forma de pagamento:
                  [1] à vista em dinheiro: 10% de desconto
                  [2] à vista no cartão: 5% de desconto
                  [3] em até 2x no cartão: preço normal
                  [4] 3x ou mais no cartão: 20% de juros
                  
                  Forma de pagamento: '''))
    
    print ('[...] REGISTRANDO FORMA DE PAGAMENTO [...]')
    sleep (2)

if item == 1:
    if forma != 1 and forma != 2 and forma != 3 and forma != 4:
        print ('[...] OPÇÃO INVÁLIDA [...]')
    else:
        print ('Parabéns, você adquiriu um CARRO no valor de R$45.000,00')
    if forma == 1:
        print ('E de acordo com sua forma de pagamento, você ganhou 10% de desconto sobre valor: R${:.2f}'.format(45000 - (45000 * 0.1)))
    elif forma == 2:
        print ('E de acordo com sua forma de pagamento, você ganhou 5% de desconto sobre valor: R${:.2f}'.format(45000 - (45000 * 0.05)))
    elif forma == 3:
        print ('E de acordo com sua forma de pagamento, você NÃO TEM desconto.')
    elif forma == 4:
        print ('E de acordo com sua forma de pagamento, você obtém 20% de acréscimos em juros: R${:.2f}'.format(45000 + (45000 * 0.2)))

elif item == 2:
    if forma != 1 and forma != 2 and forma != 3 and forma != 4:
        print ('[...] OPÇÃO INVÁLIDA [...]')
    else:
        print ('Parabéns, você adquiriu uma MOTO no valor de R$12.000,00')
    if forma == 1:
        print ('E de acordo com sua forma de pagamento, você ganhou 10% de desconto sobre o valor: R${:.2f}'.format(12000 - (12000 * 0.1)))
    elif forma == 2:
        print ('E de acordo com sua forma de pagamento, você ganhou 5% de desconto sobre o valor: R${:.2f}'.format(12000 - (12000 * 0.05)))
    elif forma == 3:
        print ('E de acordo com sua forma de pagamento, você NÃO TEM desconto.')
    elif forma == 4:
        print ('E de acordo com sua forma de pagamento, você obtém 20% de acréscimos em juros: R${:.2f}'.format(12000 + (12000 * 0.2)))

elif item == 3:
    if forma != 1 and forma != 2 and forma != 3 and forma != 4:
        print ('[...] OPÇÃO INVÁLIDA [...]')
    else:
        print ('Parabéns,você adquiriu um BARCO no valor de R$92.000,00')
    if forma == 1:
        print ('E de acordo com sua forma de pagamento, você ganhou 10% de desconto sobre o valor: R${:.2f}'.format(92000 - (92000 * 0.1)))
    elif forma == 2:
        print ('E de acordo com sua forma de pagamento, você ganhou 5% de desconte sobre o valor: R${:.2f}'.format(92000 - (92000 * 0.05)))
    elif forma == 3:
        print ('E de acordo com sua forma de pagamento, você NÃO TEM desconto.')
    elif forma == 4:
        print ('E de acordo com sua forma de pagamento, você obtém 20% de acréscimos em juros: R${:.2f}'.format(92000 + (92000 * 0.2)))
        
print ('[...] OBRIGADO POR SER NOSSO CLIENTE [...]')