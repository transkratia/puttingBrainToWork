# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres; Idade: entre 0 e 150;
# Salário: maior que zero; Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
renda = float(input("Insira seu salário: "))
sexokkkk = input("Insira seu gênero: ")
estadoCivil = input("Insira seu Estado Civil: ")

tamanhoNome = len(nome)

while tamanhoNome < 4:
    nome = input("Seu nome precisa de pelo menos 4 carácteres.\n Insira novamente: ")
    tamanhoNome = len(nome)
while idade < 0 or idade > 150:
    idade = int(input("Insira idade válida. "))
while renda <= 0:
    renda = float(input("Insira salário válido. "))
while sexokkkk != 'f' and sexokkkk != 'm' and sexokkkk != 'nb':
    sexokkkk = input("Gênero inválido. Insira novamente. ")
while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
    estadoCivil = input("Insira Estado Civil válido. ")