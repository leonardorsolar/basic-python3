# 🐍 **Tutorial para Iniciantes: Jornada de Aprendizado em Python com FastAPI**

> Este tutorial foi feito para você, que está começando com Python e deseja aprender passo a passo, desde variáveis e funções até APIs modernas com FastAPI. Siga cada aula na ordem para obter o máximo aprendizado.

---

## 📚 Visão Geral da Estrutura

```
.
├── aula01 basic               → Fundamentos da linguagem Python
├── aula02 functions           → Criação e uso de funções
├── aula03 class               → Introdução à programação orientada a objetos
├── aula04 import functions    → Como organizar funções em arquivos e importar
├── aula05 import class        → Organização e importação de classes
├── aula06 api basic get       → Criando uma API com FastAPI e método GET
├── aula07 api basic post      → Adicionando POST e estrutura mais limpa com domínio
└── README.md                  → Este tutorial que você está lendo
```

---

## 🧠 Aula 01 — Fundamentos do Python (`aula01 basic`)

### 📄 Arquivos:

-   `01main.py` – Olá mundo, variáveis e tipos básicos
-   `02operations.py` – Operações matemáticas
-   `03conditionals.py` – `if`, `else`, `elif`
-   `04list.py` – Listas e iteração
-   `05repetitions.py` – `for`, `while`
-   `06dictionaries_objects.py` – Dicionários e objetos
-   `config.md` – Explicações teóricas adicionais

> 📌 **Objetivo**: Entender a base da linguagem Python para construir sua lógica.

---

## 🔁 Aula 02 — Funções (`aula02 functions`)

### 📄 Arquivos:

-   `01functions.py` até `03functions.py` – Diferenças entre funções com/sem retorno
-   `04Classe.py` – Introdução à organização de código em blocos reutilizáveis

> 📌 **Objetivo**: Aprender a reutilizar código com funções nomeadas, com parâmetros e retorno.

---

## 🔷 Aula 03 — Classes e Objetos (`aula03 class`)

### 📄 Arquivos:

-   `01Classe.py` a `09Classe.py` – Criação de classes, atributos, métodos e herança
-   `08Interface.py` – Introdução a interfaces com `ABC`

> 📌 **Objetivo**: Introduzir a Programação Orientada a Objetos (POO), base para códigos escaláveis.

---

## 📦 Aula 04 — Importando Funções (`aula04 import functions`)

### 📁 Estrutura:

-   `main.py` – Código principal que usa funções externas
-   `utils/` – Pasta com arquivos de funções: `formatador.py`, `util.py`

> 📌 **Objetivo**: Aprender a modularizar seu projeto, separando funções por responsabilidade.

---

## 🧩 Aula 05 — Importando Classes (`aula05 import class`)

### 📁 Estrutura:

-   `domain/pessoa.py` – Classe `Pessoa`
-   `main.py` – Código que importa e utiliza a classe

> 📌 **Objetivo**: Aplicar POO na prática, organizando classes em domínios reutilizáveis.

---

## ⚙️ Aula 06 — Criando API com FastAPI - GET (`aula06 api basic get`)

### 📁 Estrutura:

-   `main.py` – API FastAPI com rotas básicas (`GET /`, `GET /hello/{nome}`)
-   `tutorial.md` – Explicação da aula

> 📌 **Objetivo**: Criar sua primeira API REST com FastAPI e testar rotas GET no navegador.

---

## 📤 Aula 07 — API FastAPI com POST e Classe Separada (`aula07 api basic post`)

### 📁 Estrutura:

-   `domain/user.py` – Classe `User`
-   `main.py` – Endpoint `POST /user` com validação Pydantic
-   `tutorial.md` – Explicação completa
-   `venv/` – Ambiente virtual com dependências

> 📌 **Objetivo**: Aprender a criar rotas POST com validação de entrada e organizar o código por domínio.

---

## 🚀 Como Rodar a API

Em qualquer aula com API:

```bash
# Ativar ambiente virtual (se tiver)
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

# Rodar servidor FastAPI
uvicorn main:app --reload
```

Abra o navegador:

-   [http://127.0.0.1:8000](http://127.0.0.1:8000)
-   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔎 Como Testar via `curl`

```bash
curl -X POST http://127.0.0.1:8000/user \
-H "Content-Type: application/json" \
-d '{"nome": "Leonardo", "idade": 25}'
```

---

## ✨ Dicas Finais

-   Sempre ative seu ambiente virtual antes de instalar bibliotecas.
-   Use o `requirements.txt` com `pip freeze > requirements.txt` para guardar as dependências.
-   Explore o Swagger gerado automaticamente para visualizar e testar as rotas.

---

## 🎓 Conclusão

Parabéns! Ao seguir essas aulas, você aprende:

✅ Fundamentos da linguagem Python
✅ Lógica com listas, condicionais e loops
✅ Funções e Programação Orientada a Objetos
✅ Organização de código com imports
✅ Criação de APIs com FastAPI (GET e POST)
