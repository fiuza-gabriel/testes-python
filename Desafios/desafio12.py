#Algoritmo que leia o preço de um produto e  mostre seu novo preço com 5% de desconto.

print('============DESAFIO 12==============')

print('Tudo com 5% OFF!!! ')

p = float(input('Digite preço do produto = R$ '))
des = p*0.05
print('Seu produto estava por R${}, agora está por R${}'.format(p,p-des)) 
