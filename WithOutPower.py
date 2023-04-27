# Faça um programa que peça dois números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

n1 = int(input("Insira a base: "))
n2 = int(input("Insira o expoente: "))
n3 = 1
n4 = n1

while n3 < n2:
    n4 = n1 * n4
    n3 += 1

print(n4)