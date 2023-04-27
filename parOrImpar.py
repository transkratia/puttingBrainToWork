# Faça um programa que peça 10 números inteiros, calcule
# e mostre a quantidade de números pares e a quantidade de
# números ímpares.

numbers = []
while len(numbers) < 10:
    x = int(input("Escreva um número: "))
    if x in numbers:
        print("Não pode escrever esse número.")
    else:
        numbers.append(x)


print(numbers)