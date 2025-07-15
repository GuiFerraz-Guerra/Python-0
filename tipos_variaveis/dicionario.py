# Declaração

pessoas = {"Guilherme": 22, "Thelma": 54, "Gabriela": 29}
print("1- Pessoas:", pessoas)

# Acessando valores por chave
print("2- Idade da Thelma:", pessoas["Thelma"])

# Adicionando uma nova chave
pessoas["Azelia"] = 80
print("3- Pessoas após adicionar Azelia:", pessoas)

# Mudando o valor de uma chave
pessoas["Azelia"] = 81
print("4- Pessoas após mudar a idade da Azelia:", pessoas)

# Removendo uma chave
del pessoas["Guilherme"]
print("5- Pessoas após remover Guilherme:", pessoas)

# keys
chave = list(pessoas.keys())
print("6- Chaves do dicionario: ", chave)
print("7- Primeira chave:", chave[0])

# values
valor = list(pessoas.values())
print("8- Valores do dicionario:", valor)
print("9- Primeiro valor:", valor[0])

# items com list
itens = list(pessoas.items())
print("10- Pares chave-valor do dicionario:", itens)
print("11- Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))

