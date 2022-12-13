#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

import math
'''
c1 = float(input(' Digite o valor do cateto adjacente:'))
c2 = float(input(' Digite o valor do cateto oposto :'))
h = math.sqrt(c1*c1+c2*c2)
r = h ** 1/2
print('Cateto adjacente: {}\nCateto oposto: {}\n Hipotenusa = {:.2f}'.format(c1, c2, h, r))
'''

# OUTRAS FORMAS DE ESCREVER
'''
c1 = float(input(' Digite o valor do cateto adjacente:'))
c2 = float(input(' Digite o valor do cateto oposto :'))
h = math.hypot(c1, c2)
print('Cateto adjacente: {}\nCateto oposto: {}\n Hipotenusa = {:.2f}'.format(c1, c2, h))
'''
c1 = float(input(' Digite o valor do cateto adjacente:'))
c2 = float(input(' Digite o valor do cateto oposto :'))

h = (c1 ** 2 + c2 ** 2)** (1/2)
print('Cateto adjacente: {}\nCateto oposto: {}\n Hipotenusa = {:.2f}'.format(c1, c2, h))
