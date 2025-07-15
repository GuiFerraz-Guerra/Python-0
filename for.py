lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)

tupla = (1,2,3,4,5)
for elemento in tupla:
    print(elemento)

dicionario = {'a': 1, 'b': 2, 'c': 3}
for chave in dicionario.keys():
    print(chave)

for valor in dicionario.values():
    print(valor)

for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')

# range(): intervalo de números
print(list(range(0,10)))

for numero in range(0, 10):
    print("Numero: ", numero)

# range com len

lista = [1,2,3,4,5]
for indice in range(0,len(lista)):
    print("Indice: ", indice)
    print("Elemento: ", lista[indice])

# mudar o valor de um elemento
listaEX = [1,2,4,4,5,6,7,8,9,10]
print(listaEX)
for indice in range(0, len(listaEX)):
    if indice == 2:
        listaEX[indice] = 3
    else:
        listaEX[indice] = 0
print(listaEX)

# enumerate
lista_enumerate = ["a", "b", "c", "d"]
for indice, valor in enumerate(lista_enumerate):
    print(f"Indice: {indice}, Valor: {valor}")
