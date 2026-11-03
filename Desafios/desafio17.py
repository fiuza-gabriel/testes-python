print('============DESAFIO 17==============')
ca = float(input('Tamanho do Cateto Adjacente = '))
co = float(input('Tamanho do Cateto Oposto = '))
hip = (ca**2) + (co**2)

print('O Cateto Oposto vale {}cm, o Cateto Ajacente {}cm. Logo o a Hipotenusa é {:.2f}cm.'.format(co,ca,hip))
