# Lista simulando um banco de dados em memória
dados = []

# Entidade ou estrutura do usuário (opcional, mas deixa mais claro)
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}')"

# Caso de uso para criar usuário
class CreateUserUseCase:
    def execute(self, name, email, password):
        user = User(name, email, password)
        dados.append(user)
        return user

# Criando o caso de uso
create_user_use_case = CreateUserUseCase()

# Executando o caso de uso
novo_usuario = create_user_use_case.execute("Leonardo", "leo@gmail.com", "123456")

# Verificando resultado
print(novo_usuario)
print(dados)


# from typing import List

# # Tipo User definido como classe comum
# class User:
#     def __init__(self, name: str, email: str, password: str):
#         self.name = name
#         self.email = email
#         self.password = password

#     def __repr__(self) -> str:
#         return f"User(name='{self.name}', email='{self.email}', password='{self.password}')"

# # Caso de uso para criar usuários
# class CreateUserUseCase:
#     def __init__(self):
#         self.dados: List[User] = []

#     def execute(self, name: str, email: str, password: str) -> User:
#         user = User(name, email, password)
#         self.dados.append(user)
#         return user

# # Criando e executando o caso de uso
# create_user_use_case = CreateUserUseCase()
# novo_usuario = create_user_use_case.execute("Leonardo", "leo@gmail.com", "123456")

# # Verificando o resultado
# print(novo_usuario)
