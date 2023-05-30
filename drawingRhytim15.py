# Escreva um algoritmo que retorne a seguinte figura. Por exemplo: x = 3

def imprimir_figura(x):
    for i in range(-x+1, x):
        espacos = abs(i)
        numeros = x - espacos

        linha = " " * espacos + "3 " * numeros
        print(linha.rstrip())

x = int(input("Digite o valor de x: "))
imprimir_figura(x)
