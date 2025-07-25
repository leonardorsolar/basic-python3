# Importa classes base para definir interfaces em Python
from abc import ABC, abstractmethod

# ========================================
# 📐 Interface para o repositório de usuários
# ========================================
class IUserRepository(ABC):
    # Método abstrato: toda classe que herdar dessa interface
    # será obrigada a implementar este método
    @abstractmethod
    def save(self, user):
        pass

    # Outro método abstrato: deve retornar todos os usuários
    @abstractmethod
    def get_all(self):
        pass


# ====================================================
# 🗄️ Repositório: simula o banco de dados em memória
# ====================================================
class UserRepository:
    def __init__(self):
        # Lista interna usada como "banco de dados"
        self.dados = []

    # Salva um usuário na lista
    def save(self, user):
        self.dados.append(user)  # Adiciona o usuário na lista
        return user  # Retorna o usuário salvo

    # Retorna todos os usuários salvos na lista
    def get_all(self):
        return self.dados
    

# ====================================================
# 🚀 Execução simples (simulando um cadastro)
# ====================================================

# Instanciando o repositório de usuários (banco simulado)
user_repository = UserRepository()

# Criando um dicionário representando um usuário
user = {
    'name': 'Leonardo',
    'email': 'leo@gmail.com',
    'password': '123456'
}

# Salvando o usuário no repositório
user_repository.save(user)

# Mostrando todos os usuários armazenados
print(user_repository.get_all())
