from abc import ABC, abstractmethod

# ============================================
# 🧱 Entidade: representa a estrutura do usuário
# ============================================
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"

# ============================================
# 🔌 Interface do Repositório (Abstração)
# ============================================
class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def get_all(self):
        pass

# ============================================
# 🗄️ Implementação concreta do Repositório
# ============================================
class UserRepository(IUserRepository):
    def __init__(self):
        self.dados = []

    def save(self, user: User):
        self.dados.append(user)
        return user

    def get_all(self):
        return self.dados

# ============================================
# 🔌 Interface do Caso de Uso (Abstração)
# ============================================
class ICreateUserUseCase(ABC):
    @abstractmethod
    def execute(self, name: str, email: str, password: str):
        pass

# ============================================
# 💡 Implementação do Caso de Uso
# ============================================
class CreateUserUseCase(ICreateUserUseCase):
    def __init__(self, repository: IUserRepository):
        self.repository = repository  # Recebe o repositório como interface (não importa a implementação)

    def execute(self, name: str, email: str, password: str):
        user = User(name, email, password)
        return self.repository.save(user)

# ============================================
# 🔌 Interface da Controller (opcional)
# ============================================
class IUserController(ABC):
    @abstractmethod
    def handle(self):
        pass

# ============================================
# 🎮 Implementação da Controller
# ============================================
class UserController(IUserController):
    def __init__(self, create_user_use_case: ICreateUserUseCase):
        self.create_user_use_case = create_user_use_case

    def handle(self):
        print("[UserController] Recebendo requisição para criar usuário...")

        # Simula entrada de dados
        data = {
            "name": "Leonardo",
            "email": "leo@gmail.com",
            "password": "123456"
        }

        # Executa o caso de uso com os dados da "requisição"
        result = self.create_user_use_case.execute(
            data["name"], data["email"], data["password"]
        )

        return {
            "message": "Usuário criado com sucesso",
            "data": repr(result)
        }

# ============================================
# 🧪 Execução: Simulação de um container simples
# ============================================

# 🔁 Instancia as implementações concretas
user_repository = UserRepository()  # Implementa IUserRepository
create_user_use_case = CreateUserUseCase(user_repository)  # Implementa ICreateUserUseCase
user_controller = UserController(create_user_use_case)  # Implementa IUserController

# 🚀 Executa o controlador simulando uma requisição
resposta = user_controller.handle()
print(resposta)

# 📦 Mostra os usuários "salvos no banco"
print("Usuários no banco:", user_repository.get_all())

for user in user_repository.get_all():
    print(user.show())