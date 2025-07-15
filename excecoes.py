print("Exemplo de captura de exceção em Python")


try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero


except ValueError as e:
    print(f"Erro de valor: {e}. Por favor, digite um número inteiro válido.")
    raise ValueError("Tipo de variavel inválido")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

else:
    print(f"O resultado da divisão é: {resultado}")

finally:
    print("Operação concluída, independente de erros.")


