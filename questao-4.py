#4- Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

dia = int(input('Digite o seu dia escolhido: '))
mes = int(input('Digite o seu mês escolhido: '))
ano = int(input('Digite o ano escolhido: '))
b = ''

if (ano % 4) == 0 and (ano % 100) == 0 and (ano % 400) == 0:
  print('O ano é bissexto!')
  b = True
elif (ano % 4) != 0:
  print('O ano não é bissexto!')
  b = False
elif (ano % 4) == 0 and (ano % 100) != 0:
  print('O ano é bissexto!')
  b = True
elif (ano % 4) == 0 and (ano % 100) == 0 and (ano % 400) != 0:
  print('O ano não é bissexto!')
  b = False