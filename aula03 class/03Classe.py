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
