# Repositório de usuários (simula um banco de dados)
class UserRepository:
    def __init__(self):
        self.dados = []

    def save(self, user):
        self.dados.append(user)
        return user

    def get_all(self):
        return self.dados


# Instanciando o repositório
user_repository = UserRepository()

#print(user_repository)

user ={
    'name': 'Leonardo',
    'email': 'leo@gmail.com',
    'password': '123456'
}

user_repository.save(user)
# Acessando os dados do repositório
print(user_repository.get_all())


# from typing import List

# # Classe para representar um usuário (sem dataclass)
# class User:
#     def __init__(self, name: str, email: str, password: str) -> None:
#         self.name = name
#         self.email = email
#         self.password = password

#     def __repr__(self) -> str:
#         return f"User(name='{self.name}', email='{self.email}', password='{self.password}')"

# # Repositório de usuários (simula um banco de dados)
# class UserRepository:
#     def __init__(self) -> None:
#         self.dados: List[User] = []

#     def save(self, user: User) -> User:
#         self.dados.append(user)
#         return user

#     def get_all(self) -> List[User]:
#         return self.dados

# # Instanciando o repositório
# user_repository = UserRepository()

# # Criando um usuário
# user = User(name='Leonardo', email='leo@gmail.com', password='123456')

# # Salvando no repositório
# user_repository.save(user)

# # Acessando os dados do repositório
# print(user_repository.get_all())


# from dataclasses import dataclass
# from typing import List

# # Classe para representar um usuário
# @dataclass
# class User:
#     name: str
#     email: str
#     password: str

# # Repositório de usuários (simula um banco de dados)
# class UserRepository:
#     def __init__(self) -> None:
#         self.dados: List[User] = []

#     def save(self, user: User) -> User:
#         self.dados.append(user)
#         return user

#     def get_all(self) -> List[User]:
#         return self.dados

# # Instanciando o repositório
# user_repository = UserRepository()

# # Criando um usuário com tipagem
# user = User(name='Leonardo', email='leo@gmail.com', password='123456')

# # Salvando no repositório
# user_repository.save(user)

# # Acessando os dados do repositório
# print(user_repository.get_all())
