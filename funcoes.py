# Exemplo
def saudacao(nome):
    return f"Olá, {nome}!"

print("\nChamando a função saudacao:")

#nome_usuario = input("Digite seu nome: ")
# ou
#saudacao("Guilherme")

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando a função quadrado: ")
resultado_quadrado = quadrado(5)
print(f"Resultado da funcao quadrado: {resultado_quadrado}")

# Função com multiplos parâmetros

def soma(a, b):
    resultado = a + b
    return resultado

print("\nChamando a função soma:")

#soma_resultado = soma(3, 4)
#print("Resultado da função soma de 3 e 4: ", soma_resultado)
# ou
#a = 10
#b = 20
#resultado_soma = soma(a, b)
#print(f"Resultado da função soma de {a} e {b}: {resultado_soma}")