# Faça um programa que peça um número inteiro positivo
# e em seguida mostre este número invertido.

n = int(input("Insira o número: "));
print(f"O número informado foi: {n}")

nInvertido = int(str(n)[::-1]);

print(f"O número invertido foi: {nInvertido}")
