PRO = 'Programa de Testes'
print('{}: Olá Mundo!'.format(PRO))
print('Eu sou o {}'.format(PRO))
NOME = input('{}: Você poderia me informa seu nome? '.format(PRO))
print('{}: Olá {} seja bem vindo ao {}!'.format(PRO, NOME, PRO))
print('{}: Por favor você poderia informar sua data de nascimento?'.format(PRO))
DIA = input('Dia: ')
MES = input('Mês: ')
ANO = input('Ano: ')
print('{}: Muito bem {} sua data de nascimento {}/{}/{}'.format(PRO, NOME, DIA, MES, ANO))
print('{}: Estou em desenvolvimento poderia me informar 2 numeros?'.format(PRO))
print('Tentarei somar um valor!')
N1 = int(input('Primeiro numero: '))
N2 = int(input('Segundo numero: '))
RE = N1 + N2
print('{}: Ok a soma entre {} e {} e igual a {}'.format(PRO, N1, N2, RE))
print('Obrigado e volte sempre!!!')

