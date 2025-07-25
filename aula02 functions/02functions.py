dados = []

def create_user(name, email, password):
    dados.append({
        'name': name,
        'email': email,
        'password': password
    })
    return dados

create_user("Leonardo", "leo@gmail", "123456")

print(dados)

create_user("Miguel", "miguel@gmail", "123456")

print("resposta",dados)