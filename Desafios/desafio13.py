#Algoritmo que leia o salário do funcionário e mostre seu novo salário com 15% de aumento.

print('============DESAFIO 13==============')

print('15% de aumento vamos ver quanto isso dá?')

s = float(input('Digite seu salário = R$ '))
a = (s*0.15) + s

print('Seu salário vai para R${} após o aumento.'.format(a))
