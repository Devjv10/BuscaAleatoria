function f(x) {
  return x * x; // x²
}

// Gera 100 valores aleatórios de uma vez
const xs = Array.from({ length: 100 }, () => Math.random() * 20 - 10);

// Usa reduce para encontrar o mínimo em uma única passada
const melhorX = xs.reduce((melhor, atual) =>
  f(atual) < f(melhor) ? atual : melhor
);

const melhorValor = f(melhorX);

console.log("Melhor x encontrado:", melhorX);
console.log("Menor valor da função:", melhorValor);
