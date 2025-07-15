# Exemplo if
idade = 18
if idade >= 18:
    print("Você é maior de idade.")

if idade < 18:
    print("Você é menor de idade.")

if idade == 18:
    print("Você tem exatamente 18 anos.")

if idade != 18:
    print("Você não tem 18 anos.")

# Exemplo if-else | if-elif-else

if idade >= 18:
    print("Você é maior de idade.")
elif idade == 17:
    print("Você é quase maior de idade.")
else:
    print("Você é menor de idade.")


mensagem = "Você é maior de idade." if idade >= 18 else "Você é menor de idade."
print(mensagem)