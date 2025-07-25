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

