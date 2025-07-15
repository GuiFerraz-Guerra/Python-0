print('Exemplo de importação de um modulo padrão do Python')

## Importando o módulo math para calcular a raiz quadrada
import math
## Importando apenas a função sqrt do módulo math
from math import sqrt

raiz = sqrt(81)
print(f"A raiz quadrada de 81 é: {raiz}")

## Importando um módulo personalizado
import meu_modulo

# Importando funções específicas do módulo personalizado
from meu_modulo import saudacao, dobro

mensagem = meu_modulo.saudacao("Guilherme")
resultado = meu_modulo.dobro(5)
print(mensagem)
print(f"O dobro de 5 é: {resultado}")