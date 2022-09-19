#1 - Faça um programa para leitura de três notas parciais de um aluno.

nota1 = int(input('Digite a nota 1:'))
print(nota1)
nota2 = int(input('Digite a nota 2:'))
print(nota2)
media = (nota1 + nota2)/2
print("A média é igual a: ", media)

if media >= 7 and media < 10:
  print("Parabéns, você foi APROVADO com a média", media)
elif media == 10:
  print("Parabéns, você foi APROVADO COM DISTINÇÃO", media)
else:
  print("Você foi REPROVADO", media)