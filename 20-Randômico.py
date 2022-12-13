# um professor deseja escolher a ordem de apresntação dos alunos. Faça um programa que leia o nome e escolha a ordem de apresentação:
import random
a1 = str(input(' Digite o nome do primeiro aluno:'))
a2 = str(input(' Digite o nome do segundo aluno: '))
a3 = str(input(' Digite o nome do terceiro aluno: '))
a4 = str(input(' Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]

random.shuffle(lista)
print(' A ordem de apresentação será: {}'.format(lista))
