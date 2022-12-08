# Faça um programa que leia o preço de um produto e mostre um novo preço com 5% de desconto

input('olá, seja bem vindo!')
p1 = float(input('Digite o valor real do produto por gentileza: R$ '))
p2 = p1*5/100
p3 = p1-p2


print('Parabéns, você recebeu 5% de desconto neste produto')
print(' De R${} por apenas R${:.2f}'.format(p1, p3))
