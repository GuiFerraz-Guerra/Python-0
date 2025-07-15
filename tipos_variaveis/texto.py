# Declaração
nome_completo = "Guilherme Guerra"

nome = "Guilherme"
sobrenome = "Guerra"

nome_quebrado = "Guilherme \
Guerra"

# Formatação de strings

print("1- Nome completo: ", nome_completo)
print("2- Nome: " + nome)
print("3- Nome Completo: ", nome + " " + sobrenome)
print("4- Nome Completo: ", nome_quebrado)

# f-strings
print("5- Nome Completo: %s" % nome_completo)
print("6- Nome Completo: %s %s" % (nome, sobrenome))
print(f"7- Nome Completo: {nome} {sobrenome}")
print("8- Nome Completo: {} {}".format(nome, sobrenome))

# upper
print("9- Nome Completo: ", nome_completo.upper())

# lower
print("10- Nome Completo: ", nome_completo.lower())

# count
print("11- Nome Completo: ", nome_completo.count("G"))

# find
print("12- Nome Completo: ", nome_completo.find("i"))

# encode
print("13- Nome Completo: ", nome_completo.encode())

# decode
print("14- Nome Completo: ", nome_completo.encode().decode())

# replace
print("15- Nome Completo: ", nome_completo.replace("Guerra", "Ferraz"))

# split
print("16- Nome Completo: ", nome_completo.split(" "))

# strip
print("17- Nome Completo: ", nome_completo.strip())

# rstrip
print("18- Nome Completo: ", nome_completo.rstrip())

# startwith
print("19- Nome Completo: ", nome_completo.startswith("Guilherme"))

# in ou not in
print("20- Nome Completo: ", "Guerra" in nome_completo)
print("21- Nome Completo: ", "Guerra" not in nome_completo)