# Entidade: estrutura do usuário
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}')"

# Repositório de usuários (simula um banco de dados)
class UserRepository:
    def __init__(self):
        self.dados = []

    def save(self, user):
        self.dados.append(user)
        return user

    def get_all(self):
        return self.dados

# Caso de uso para criar usuário
class CreateUserUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, name, email, password):
        user = User(name, email, password)
        result = self.repository.save(user)
        return result

# Instanciando o repositório e o caso de uso
user_repository = UserRepository()
create_user_use_case = CreateUserUseCase(user_repository)

# Executando o caso de uso
novo_usuario = create_user_use_case.execute("Leonardo", "leo@gmail.com", "123456")
# user ={
#     'name': 'Leonardo',
#     'email': 'leo@gmail.com',
#     'password': '123456'
# }
# novo_usuario = create_user_use_case.execute(user['name'], user['email'], user['password'])

# Verificando resultado
print(novo_usuario)
print(user_repository.get_all())

