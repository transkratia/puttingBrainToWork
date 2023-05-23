# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.

qtd_pares = 0
qtd_impares = 0

for i in range(10):
    num = int(input(f"Informe o {i+1}° número: "))
    if num % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

print(f"A quantidade de pares é {qtd_pares}")
print(f"A quantidade de pares é {qtd_impares}")