print('============DESAFIO 18==============')
print('Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
import math
angulo = float(input('Angulo desejado: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(' O ângulo {} tem seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))
