# Faça um algoritmo que leia o preço de um 
# produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('digite o preco?R$'))
desconto = preco - (preco*5/100)
print('o valor original é {:.2f} com desconto ficará {:.2f}!'.format(preco, desconto))