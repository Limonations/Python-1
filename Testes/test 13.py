#Faça um algoritmo que leia o salário de um funcionário 
# e mostre seu novo salário, com 15% de aumento.
salario = float (input ('digite seu salario? R$'))
novo = salario + (salario*15/100)
print('seu salario de {:.2f} ficará {:.2f}!'.format(salario, novo))