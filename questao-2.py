#2- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input('Digite uma nota entre 0 e 10: '))

if (nota == 0) and (nota <= 10):
  print('Sua nota é: ' + nota)
while (nota < 0) or (nota > 10) :
  print(input('Nota inválida! Digite uma nota entre 0 e 10!'))
  break