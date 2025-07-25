dados = []

def createUser(response):
    dados.append({
        'name': response['name'],
        'email': response['email'],
        'password': response['password']
    })
    return dados

objetoFrontResponse = {
    'name': 'Leonardo',
    'email': 'leo@gmail',
    'password': '123456'
}

createUser(objetoFrontResponse)

print(dados)

