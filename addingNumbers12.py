# Faça um programa que mostre os n termos da Série a seguir:
#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.


def calcular_serie(n):
    soma = 0.0
    m = 1
    for i in range(1, n + 1):
        termo = i / m
        soma += termo
        m += 2
        print(f'Termo {i}: {termo}')

    print(f'Soma da série: {soma}')


n = int(input('Digite a quantidade de termos desejada: '))
calcular_serie(n)

