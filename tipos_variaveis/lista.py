# Declaração
minha_Lista = [1, 2, 3, 4, 5, "lista1"]
print("1- Minha Lista:", minha_Lista)

# Exibindo um indice específico
print("2- Exibindo o indice 0:", minha_Lista[0])

# Exibindo um intervalo de indices
print("3- Exibindo os indices de 0 a 4:", minha_Lista[0:5])

# Mudando o indice 0
minha_Lista[0] = 10
print("4- Mudando o indice 0:", minha_Lista)

# append
minha_Lista.append(6)
print("5- Adicionando o valor 6:", minha_Lista)

# index
print("6- Exibindo o indice do valor 10:", minha_Lista.index(10))

# insert
minha_Lista.insert(0, 20)

# pop
elemento_removido = minha_Lista.pop(0)
print("7- Exibindo o indice 0:", minha_Lista)

# remove
minha_Lista.remove("lista1")
print("8- Removendo o valor 'lista1':", minha_Lista)

# sort
minha_Lista.sort()
print("9- Ordenando a lista:", minha_Lista)

