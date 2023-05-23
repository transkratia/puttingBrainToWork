# Faça um programa que calcule o número médio de alunos por turma. Para isto,
# peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

nTurmas = int(input("Há quantas turmas? "))
nAlunosGeral = 0

for i in range(nTurmas):
    
    nAlunos = int(input(f"Quantos alunos tem na turma {i+1}? "))
    
    while nAlunos > 40:
        print("Número inválido.")
        nAlunos = int(input("Insira outro número. "))

    nAlunosGeral += nAlunos

print(f"Há {nAlunosGeral/nTurmas} para cada {nTurmas} turmas.")
