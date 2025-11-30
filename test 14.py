# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float ( input('digite a temperatura Cº'))
f = ((9*c)/5)+32
k = c + 273,15
print('A temperatura em C é {}, já em farenheit é {} e em Kelvin é {}'.format(c, f, k))