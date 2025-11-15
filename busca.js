function f(x) {
  return x * x; // x²
}

let melhorX = null;
let melhorValor = Infinity;

for (let i = 0; i < 100; i++) {
  const x = Math.random() * 20 - 10; // número entre -10 e 10
  const valor = f(x);

  if (valor < melhorValor) {
    melhorValor = valor;
    melhorX = x;
  }
}

console.log("Melhor x encontrado:", melhorX);
console.log("Menor valor da função:", melhorValor);
