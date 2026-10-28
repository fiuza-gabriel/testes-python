#Leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessário para pintar. Tinta:2m²

print('============DESAFIO 11==============')

b = float(input('Largura da Parede = '))
h = float(input('Altura da Parede = '))
t = 2

print('Sua parede tem {}m de largura e {}m de altura. Então tem {}m².' .format(b, h, b * h))
print('Para pintar a parede é necessário {}L de tinta.' .format((b*h)/t))
