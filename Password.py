import random


print('Gerador de senha')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()?0123456789'

number = input('Quantas senhas: ')
number = int(number)

length = input('O tamanho da senha: ')
length = int(length)

print('\nAqui estão as senhas:')

for pwd in range(number):
    passwords = ''
    for c in range (length):
        passwords += random.choice(chars)
    print(passwords)