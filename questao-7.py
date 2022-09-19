#7- Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.

def reverso (num):
  return str (num[::-1])

num = str(input('Informe um número: '))
print(f' Reverso: {reverso(num)}')