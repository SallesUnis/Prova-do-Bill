print('-'*40)
print('Exercício 2 - Sequência de Fibonacci')
print('-'*40)
n = int(input('Escreva o númeo desejado: '))
t1 = 0
t2 = 1
print('-'*40)
print('{} - {}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - Fim da sequência')
print('-'*40)