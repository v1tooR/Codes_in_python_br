from os import system
import os


def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y

print("Selecione uma operacao:")
print("1.Adicao")
print("2.Subtracao")
print("3.Multiplicacao")
print("4.Divisao")

while True: #Não terá nenhum parâmetro para impedir o laço, tendo que criar um "if" opicional para o usuário querer terminar ou não
    choice = input("Escolha entre 1,2,3,4: ")

    if choice in ('1','2','3','4'):
        num1 = float(input("Coloque um numero: "))
        num2 = float(input("Coloque o segundo numero: "))

        if choice == '1':
            print(num1,"+", num2, "=", add(num1,num2))
            

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1,num2))
        
        elif choice == '3':
            print(num1, "*", num2, "=", mult(num1,num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1,num2))

        next_calculation = input("Quer outra operação (yes/no): ")
        if next_calculation == "no":
                break
        else:
            print("Vamos continuar!")