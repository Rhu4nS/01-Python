# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira.
'''
import math
num = float(input(' Digite um numero:'))
v = round(num)
print(' O número inteiro é: {}'.format(v))
'''

'''
# Outras formas de escrever:

from math import trunc
num = float(input(' Digite um numero:'))
print(' O número digitado é: {} e sua porção inteira é: {}'.format(num, trunc(num)))
'''
num = float(input(' Digite um numero:'))
print(' O número digitado é: {} e sua porção inteira é: {}'.format(num, int(num)))