# Faça um programa que leia um nome de usuário
# e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

user = input("Insira o nome de usuário: ")
password = input("Insira a senha de usuário: ")

while user == password:
    print(f"ERROR: {user} e {password} não podem coincidir.\n Insira novamente as informações.")
    user = input("Insira o nome de usuário: ")
    password = input("Insira a senha de usuário: ")