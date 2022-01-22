nome = str(input('Qual é o seu nome? '))
if nome == 'Maykel':
    print ('Que nome lindo!')
elif nome == 'Marcos' or nome == 'Jaqueline' or nome == 'Miguel':
    print ('Eu acho que conheço você!')
# A função 'elif' é a junção entre 'else' e 'if', ou seja 'senão se'
elif nome in 'Maria Vitória Zezé':
    print ('Eu vi você ontem no Cabo.')
else:
    print ('Seu nome é bem comum!')

print ('Tenha uma boa noite, {}.'.format(nome))
