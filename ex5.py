print('-'*40)
print('Exercício 5 - Tamanho de Bytes')
print('-'*40)

ask = str(input('Bem Vindo, gostaria de saber quantos caracteres tem em alguns de seus dados? '))
if ask == 'sim' or 'Sim':
    nome = str(input("Insira seu nome: "))
    número = (input("Insira seu telefone: "))
    email = str(input("Insira seu e-mail: "))
    print('-' * 40)
    print('Seu nome: ',end='')
    print(len(nome))
    print('-' * 40)
    print('Seu Telefone: ', end='')
    print(len(número))
    print('-' * 40)
    print('Seu E-Mail: ', end='')
    print(len(email))
    print('-' * 40)
else:
    print('vai ter que rodar o app novamente então')
