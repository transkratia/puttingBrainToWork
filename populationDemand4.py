# Faça um programa que calcule e escreva o número de anos necessários
# para que a população do país A (80.000) ultrapasse ou iguale a população do
# país B (200.000), mantidas as taxas de crescimento (3%, 1.5%).

a = int(input("Insira a população de país A: "))
b = int(input("Insira a população de país B: "))
t1 = float(input("Insira a taxa de crescimento de país A, ao ano: "))
t2 = float(input("Insira a taxa de crescimento de país B, ao ano: "))
contador = 0

while a <= b:
    a = a + a * t1/100
    b = b + b * t2/100
    contador += 1

print(f"Demorará {contador} para a população de A superar B")