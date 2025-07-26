## Aula 02

Se você quisesse **tipar esse código Python**, pode usar **`list[dict[str, str]]`** ou `List[Dict[str, str]]` com `typing`. Aqui está o mesmo código com **tipagem estática em Python**:

```python
from typing import List, Dict

# Lista de dicionários com tipagem
dados: List[Dict[str, str]] = []

# Função com parâmetros tipados e retorno tipado
def create_user(name: str, email: str, password: str) -> List[Dict[str, str]]:
    dados.append({
        'name': name,
        'email': email,
        'password': password
    })
    return dados

# Chamadas da função
create_user("Leonardo", "leo@gmail", "123456")
print(dados)

create_user("Miguel", "miguel@gmail", "123456")
print("resposta", dados)
```

### ✔️ Explicações:

-   `List[Dict[str, str]]` indica uma lista onde cada item é um dicionário com **chaves e valores do tipo `str`**.
-   É necessário importar os tipos `List` e `Dict` do módulo `typing`.

Se quiser deixar ainda mais robusto, você pode criar um `TypedDict` ou até usar `dataclass`.

# aula 03

Aqui está seu código em Python com **tipagem explícita**, utilizando `TypedDict` para garantir a estrutura do objeto `response`, além da tipagem da lista `dados`:

```python
from typing import List, Dict, TypedDict

# Definindo a estrutura esperada para os dados do usuário
class UserInput(TypedDict):
    name: str
    email: str
    password: str

# Lista tipada de usuários
dados: List[UserInput] = []

# Função com tipagem
def createUser(response: UserInput) -> List[UserInput]:
    dados.append({
        'name': response['name'],
        'email': response['email'],
        'password': response['password']
    })
    return dados

# Simulando os dados recebidos do frontend
objetoFrontResponse: UserInput = {
    'name': 'Leonardo',
    'email': 'leo@gmail',
    'password': '123456'
}

# Chamando a função e exibindo os dados
createUser(objetoFrontResponse)
print(dados)
```

### ✅ O que foi usado:

-   `TypedDict`: para definir o formato de `response` como um dicionário com campos específicos (`name`, `email`, `password`).
-   `List[UserInput]`: indica que `dados` é uma lista contendo objetos com a estrutura de `UserInput`.

Se quiser que os dados sejam representados como objetos em vez de dicionários, podemos usar `dataclasses`. Deseja esse modelo também?

# aula 04:

Aqui está o seu código Python com **tipagem explícita** usando `type hints`:

```python
class User:
    def __init__(self, name: str, email: str, password: str) -> None:
        self.name: str = name
        self.email: str = email
        self.password: str = password

# Criando o objeto
user = User("Leonardo", "leo@gmail", "123456")

# Acessando os atributos
print(user.name)
print(user.email)
print(user.password)
print(user)
```

### ✅ Explicações:

-   `name: str`, `email: str`, `password: str`: tipagem dos parâmetros.
-   `-> None`: indica que o construtor (`__init__`) não retorna nada.
-   Atribuímos tipos também aos atributos dentro da classe (opcional, mas mais explícito).

Se quiser deixar a classe ainda mais segura, dá para usar `@dataclass` também.
