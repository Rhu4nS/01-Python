'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas e minusculas
- Quantas letras ao todo (sem contar os espaços)
- Quantas letras tem o primeiro nome
'''


nome = str(input('Digite seu nome completo : ')).strip()
dividido= nome.split()
print('Analisando seu nome... ')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(dividido[0].title(), len(dividido[0])))

# OUTRA FORMA DE ESCREVER:

nome = str(input('Digite seu nome completo : ')).strip()
print('Analisando seu nome... ')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
