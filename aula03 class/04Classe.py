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

