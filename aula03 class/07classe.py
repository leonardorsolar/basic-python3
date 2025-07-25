# ============================================
# Entidade: classe User
# Repositório: classe UserRepository
# Caso de uso: classe CreateUserUseCase
# Controller: classe UserController
# ============================================


# ============================================
# 🧱 Entidade: representa a estrutura do usuário
# ============================================
class User:
    def __init__(self, name, email, password):
        self.name = name              # Nome do usuário
        self.email = email            # Email do usuário
        self.password = password      # Senha do usuário

    # Método especial para exibir o usuário de forma legível
    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"


# ====================================================
# 🗄️ Repositório: simula o banco de dados em memória
# ====================================================
class UserRepository:
    def __init__(self):
        # Lista interna que armazenará os usuários
        self.dados = []

    # Salva um usuário no "banco" (lista)
    def save(self, user):
        self.dados.append(user)
        return user  # Retorna o usuário salvo

    # Retorna todos os usuários cadastrados
    def get_all(self):
        return self.dados


# =====================================================
# 💡 Caso de Uso: regra de negócio para criar um usuário
# =====================================================
class CreateUserUseCase:
    def __init__(self, repository):
        # Recebe o repositório onde os dados serão salvos
        self.repository = repository

    def execute(self, name, email, password):
        # Cria uma nova instância da entidade User
        user = User(name, email, password)

        # Salva o usuário no repositório
        result = self.repository.save(user)

        # Retorna o usuário criado
        return result


# =====================================================
# 🎮 Controller: simula a entrada de dados de uma "requisição"
# =====================================================
class UserController:
    def __init__(self, create_user_use_case):
        # Recebe o caso de uso como dependência (injeção de dependência)
        self.create_user_use_case = create_user_use_case

    def handle(self):
        print("[UserController] Recebendo requisição para criar usuário...")

        # Simula dados recebidos de uma requisição
        data = {
            "name": "Leonardo",
            "email": "leo@gmail.com",
            "password": "123456"
        }

        # Executa o caso de uso com os dados simulados
        result = self.create_user_use_case.execute(
            data["name"], data["email"], data["password"]
        )

        # Retorna uma resposta simulada (como se fosse um JSON)
        return {
            "message": "Usuário criado com sucesso",
            "data": repr(result)  # Usa __repr__ da classe User
        }


# ============================================
# 🧪 Execução (simula a aplicação rodando)
# ============================================

# Instancia o repositório (simula um banco de dados)
user_repository = UserRepository()

# Instancia o caso de uso passando o repositório
create_user_use_case = CreateUserUseCase(user_repository)

# Instancia a controller passando o caso de uso
user_controller = UserController(create_user_use_case)

# Simula o envio da requisição e exibe a resposta
resposta = user_controller.handle()
print(resposta)

# 🖨️ Exibe todos os usuários cadastrados no "banco"
print("Usuários no banco:", user_repository.get_all())


