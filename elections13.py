# Programa dos votos. Eu me esforcei nesse.

candidatos = {1: "Jose", 2: "João", 3: "Maria", 4: "Ana"}
votos_candidatos = {candidato: 0 for candidato in candidatos}
votos_nulos = 0
votos_brancos = 0

num_pessoas = int(input("Digite o número de pessoas que irão votar: "))

for _ in range(num_pessoas):
    voto = int(input("Digite o código do candidato (ou 5 para Nulo, 6 para Branco): "))

    if voto in votos_candidatos:
        votos_candidatos[voto] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
    else:
        print("Código inválido!")

total_votos = sum(votos_candidatos.values()) + votos_nulos + votos_brancos

print("\nResultado da Eleição")
print("--------------------")
print("Candidatos:")
for candidato, votos in candidatos.items():
    print(f"{candidato}: {votos} - {votos_candidatos[candidato]} votos")

print(f"Votos Nulos: {votos_nulos} votos")
print(f"Votos em Branco: {votos_brancos} votos")

porcentagem_nulos = (votos_nulos / total_votos) * 100
porcentagem_brancos = (votos_brancos / total_votos) * 100

print(f"Percentagem de votos nulos: {porcentagem_nulos:.2f}%")
print(f"Percentagem de votos em branco: {porcentagem_brancos:.2f}%")
