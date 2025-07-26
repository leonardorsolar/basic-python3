class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Criando o objeto
user = User("Leonardo", "leo@gmail", "123456")

# Acessando os atributos
print(user.name)
print(user.email)
print(user.password)
print(user)


# class User:
#     def __init__(self, name: str, email: str, password: str) -> None:
#         self.name: str = name
#         self.email: str = email
#         self.password: str = password

# # Criando o objeto
# user = User("Leonardo", "leo@gmail", "123456")

# # Acessando os atributos
# print(user.name)
# print(user.email)
# print(user.password)
# print(user)
# print(user.__dict__)  # Exibe os atributos do objeto como um dicionário
# print(type(user))  # Exibe o tipo do objeto
# print(isinstance(user, User))  # Verifica se user é uma instância da classe
# print(isinstance(user, object))  # Verifica se user é uma instância de object
# print(isinstance(user, str))  # Verifica se user é uma instância de str

