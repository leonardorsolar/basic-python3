lista_numeros = [1, 2, 3, 4, 5]
print("Lista de números:", lista_numeros)
print("Lista de números:", lista_numeros[0])

lista_strings = ["Python", "Java", "C++"]
print("Lista de strings:", lista_strings)

lista_vazia = []
print("Lista vazia:", lista_vazia)
print("Tamanho da lista de números:", len(lista_vazia))
lista_vazia.append(6)
print("Lista de números após adicionar 6:", lista_vazia)

# métodos de lista
lista_numeros.append(6)
print("Lista de números após adicionar 6:", lista_numeros)
lista_numeros.remove(2)
print("Lista de números após remover 2:", lista_numeros)
print("---x-----x---")
lista_numeros.reverse()
print("Lista de números invertida:", lista_numeros)
lista_numeros.sort()
print("Lista de números ordenada:", lista_numeros)
print("Lista de números:", lista_numeros)
print("Primeiro elemento da lista de números:", lista_numeros[0])
print("Último elemento da lista de números:", lista_numeros[-1])
print("---x-----x---")
print("total:", len(lista_numeros))
print("menor valor:", min(lista_numeros))
print("maior valor:", max(lista_numeros))
print("---x-----x---")
print("Lista de números:", lista_numeros)
lista_numeros.pop(1)
print("Lista de números:", lista_numeros)
print("---x-----x---")
print("Soma dos elementos da lista de números:", sum(lista_numeros))
print("Média dos elementos da lista de números:", sum(lista_numeros) / len(lista_numeros))