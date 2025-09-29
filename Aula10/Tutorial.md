# Simple FastAPI Example

## ✅ 3. Instale as bibliotecas necessárias

É uma boa prática criar um ambiente virtual só para o projeto:

Se ainda não tiver um ambiente virtual, crie um:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Agora instale o FastAPI e o servidor:

Rodar o comando de instalação

Se você já tem o Python e o pip instalados:

```bash
pip install -r requirements.txt
```

Isso vai ler o arquivo requirements.txt e instalar todos os pacotes listados.

ou se quer isntalar cada biblioteca

```bash
pip install fastapi uvicorn
```

---

## ✅ 4. Adicione o arquivo `.gitignore` (opcional, mas recomendado)

Crie um arquivo `.gitignore`:

```bash
touch .gitignore
```

E adicione o seguinte conteúdo:

```
__pycache__/
*.pyc
*.pyo
venv/
.env/
```

---

## ✅ 5. Execute o servidor localmente

No terminal, dentro da pasta `meu_app`, rode:

```bash
uvicorn 01main:app --reload
```

ou

```bash
uvicorn 01main:app --reload --port 8005
```

> Esse comando diz ao Uvicorn para rodar:
>
> -   `main`: o nome do arquivo `main.py`
> -   `app`: a instância do FastAPI
> -   `--reload`: recarrega o servidor automaticamente quando o código muda (ótimo para desenvolvimento)

---

## ✅ 6. Acesse sua API no navegador

-   Endpoint raiz:
    👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

-   Documentação automática:
    👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

https://www.youtube.com/watch?v=iWS9ogMPOI0
