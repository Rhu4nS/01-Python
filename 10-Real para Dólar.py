
crie um programa que mostre quanto de dinheiro uma pessoa tem na carteira e quantos dolares ela consegue comprar
considerando: US$ 1,00= 3,27


r = float(input('Quantos reais você tem na carteira? R$'))
d = r/3.27

print(' Com R${:.2f}, você consegue comprar US${:.2f}'.format(r, d))
