#Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse angulo.

import math

a = int(input(' Digite o valor do angulo: '))

c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))
print('Angulo:{}\nO valor do cosseno é: {:.2f}\n O valor do seno é: {:.2f}\n O valor da tangente é igual a: {:.2f}'.format( a, c, s, t))