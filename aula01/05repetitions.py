for x in range(9):
    print(x)
print("---x---")

for x in range(5):
    print("Repetição número:", x + 1)
print("Repetições concluídas.")


bancodedados = []

for x in range(2):
    nome = input("Digite seu nome: ")
    password = int(input("Digite a senha: "))
    bancodedados.append((nome, password))
    print("Dados inseridos no banco de dados:", bancodedados)