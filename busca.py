import random
import math

# Função que queremos minimizar
def f(x):
    return x**2 + 10 * math.sin(x)

# Constantes
LIMITE_INFERIOR = -10
LIMITE_SUPERIOR = 10
ITERACOES = 100

# Busca aleatória
melhor_x = None
melhor_valor = float("inf")

for i in range(ITERACOES):
    x = random.uniform(LIMITE_INFERIOR, LIMITE_SUPERIOR)
    valor = f(x)

    if valor < melhor_valor:
        melhor_x = x
        melhor_valor = valor

print("Melhor x encontrado:", melhor_x)
print("Valor de f(x):", melhor_valor)
