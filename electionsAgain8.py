# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

Bolsonaro = 0
Lula = 0
Ciro = 0

nEleitor = int(input("Há quantos eleitores? "))

for i in range(nEleitor):
    nVotos = int(input("Insira o número do candidato. "))
    if nVotos == 13:
        Lula += 1
    elif nVotos == 12:
        Ciro += 1
    elif nVotos == 22:
        Bolsonaro += 1

print(f"O resultado das urnas apuradas foi de {Bolsonaro, Lula, Ciro}")