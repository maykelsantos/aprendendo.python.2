from time import sleep
valorcasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar? '))
meses = anos * 12
parcelas = valorcasa / meses
print ('PROCESSANDO OS DADOS [...]')
sleep (3)
if parcelas > (salario * 0.3):
    print ('***EMPRÉSTIMO NEGADO***')
    print ('Obrigado por utilizar nossos serviços.')
else:
    print ('***EMPRÉSTIMO APROVADO***')
    print ('Você pagará {} parcelas de R${:.2f} mensais.'.format(meses, parcelas))
