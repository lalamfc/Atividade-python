#3- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

tempF = float(input("Informe a temperatura em graus Fahrenheit: "))
tempC = round(5 * ((tempF - 32)/9),2)
print('Sua temperatura em Celsius é: ' + str (tempC))
