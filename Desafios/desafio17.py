print('============DESAFIO 17==============')
import math
ca = float(input('Tamanho do Cateto Adjacente = '))
co = float(input('Tamanho do Cateto Oposto = '))
hip = math.hypot(ca, co)

print('O Cateto Oposto vale {}cm, o Cateto Ajacente {}cm. Logo o a Hipotenusa é {:.2f}cm.'.format(co,ca,hip))
