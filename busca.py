import random

# Função simples para minimizar
def f(x):
    return x * x  # x²

melhor_x = None
melhor_valor = float("inf")

for _ in range(100):
    x = random.uniform(-10, 10)  # sorteia um número aleatório
    valor = f(x)                 # calcula f(x)

    if valor < melhor_valor:     # verifica se é o melhor até agora
        melhor_x = x
        melhor_valor = valor

print("Melhor x encontrado:", melhor_x)
print("Menor valor da função:", melhor_valor)
