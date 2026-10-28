#Crie um programa que leia quanto tem na carteira e mostre quantos dólares pode comprar Dólar: 3,27

print('============DESAFIO 10==============')
real = float(input('Quanto você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R$ {} você pode comprar US$ {:.2f}'.format(real, dolar))