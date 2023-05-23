# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário,
# conforme exemplo abaixo:

# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

nMult = int(input("Que número deve ser multiplicado? "))
nIni = int(input("Deve começar a ser multiplicado por quanto? "))
nFin = int(input("Deve terminar de ser multiplicado por quanto? "))

# Se nIni > nFim:

if nFin < nIni:
    nIni, nFin = nFin, nIni

for i in range(nIni, nFin+1):
    print(f"{nMult} X {i} = {(nMult*i)}")