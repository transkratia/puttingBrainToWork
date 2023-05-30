# Dado um número inteiro de entrada do usuário de quatro dígitos, imprima se este é um palíndromo ou não. Por exemplo: 1441 é um palíndromo, 1231 não é um palíndromo.

numero = int(input("Digite um número inteiro de quatro dígitos: "))

# Separação dos dígitos do número
digito1 = numero // 1000
digito2 = (numero // 100) % 10
digito3 = (numero // 10) % 10
digito4 = numero % 10

if digito1 == digito4 and digito2 == digito3:
    print("O número é um palíndromo!")
else:
    print("O número não é um palíndromo!")
