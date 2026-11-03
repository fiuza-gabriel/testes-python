print('============DESAFIO 20==============')
print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')

import random
alunos = ['Arthur', 'Gabriel', 'Maria', 'Rachel']
random.shuffle(alunos)
print('A ordem das apresentações será: {}.'.format(alunos))
