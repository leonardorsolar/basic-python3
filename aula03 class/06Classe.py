class UserController:

    def handle(self):
        print("[UserController] Recebendo requisição...")

        # Simulando dados de entrada (como se viessem do frontend ou API)
        data = {
            "name": "Leonardo",
            "email": "leo@gmail.com",
            "password": "123456"
        }

        # Chamando o caso de uso com os dados
        result_response = data
        return {
            "message": "Usuário criado com sucesso",
            "data": result_response
        }


# Instanciando o controlador
user_controller = UserController()
# Executando o controlador
response = user_controller.handle()
# Verificando a resposta
print(response)
print("Usuário criado com sucesso:", response['data'])


# from typing import Dict, Any


# class UserController:

#     def handle(self) -> Dict[str, Any]:
#         print("[UserController] Recebendo requisição...")

#         # Simulando dados de entrada (como se viessem do frontend ou API)
#         data: Dict[str, str] = {
#             "name": "Leonardo",
#             "email": "leo@gmail.com",
#             "password": "123456"
#         }

#         # Chamando o caso de uso com os dados
#         result_response: Dict[str, str] = data

#         return {
#             "message": "Usuário criado com sucesso",
#             "data": result_response
#         }


# # Instanciando o controlador
# user_controller: UserController = UserController()

# # Executando o controlador
# response: Dict[str, Any] = user_controller.handle()

# # Verificando a resposta
# print(response)
# print("Usuário criado com sucesso:", response['data'])
