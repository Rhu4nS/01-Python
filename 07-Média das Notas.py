# desenvolva um programa que mostre duas notas e mostre a media entre elas:

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
m= (n1+n2)/2

print(' Sua primeira nota foi: {:.1f}\n Sua segunda nota foi: {:.1f}\n Sua média final foi: {:.1f}'.format(n1, n2, m))

#outro jeito de escrever:

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
print(' Sua primeira nota foi: {}\n Sua segunda nota foi: {}\n Sua média final foi: {}'.format(n1, n2, ((n1+n2)/2)))


if m >= 6:
    print('parabéns, você está aprovado!')
else:
    print('Sinto muito, você está reprovado')
