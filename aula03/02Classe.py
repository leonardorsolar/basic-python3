# Lista simulando um banco de dados em memória
dados = []

class CreateUserUseCase:
    def execute(self, name, email, password):
        user = {
           'name': name,
           'email': email,
           'password': password
        }
        dados.append(user)
        return user

# Criando o caso de uso
create_user_use_case = CreateUserUseCase()

# Executando o caso de uso
novo_usuario = create_user_use_case.execute("Leonardo", "leo@gmail.com", "123456")

# Verificando resultado
print(novo_usuario)
