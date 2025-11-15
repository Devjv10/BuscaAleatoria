✔ 1. Substituição do for por Array.from

Gero os 100 números aleatórios em uma única operação.

Evita criar variáveis temporárias a cada iteração.

✔ 2. Uso de reduce

O método reduce percorre a lista apenas uma vez e seleciona o melhor valor.

O mecanismo interno é otimizado pela engine JavaScript (V8).

✔ 3. Menos operações dentro do loop

Na versão original, toda iteração faz:

criação de variável

comparação

atribuição condicional

Na nova versão, apenas compara diretamente via reduce.

✔ 4. Código mais simples e mais legível

A lógica da busca aleatória fica em apenas duas linhas:

gerar a lista

achar o mínimo

✅ Resumo do Trabalho — Busca Aleatória

A busca aleatória é um método simples de otimização no qual o algoritmo testa várias soluções geradas ao acaso dentro de um intervalo e escolhe aquela que produz o menor valor de uma função. É um processo sem estratégia de direcionamento: cada tentativa é independente e não utiliza informações das anteriores. Apesar de simples, é útil como baseline e para funções onde métodos tradicionais têm dificuldade.

No trabalho, implementamos esse algoritmo em JavaScript para minimizar a função 

f(x)=x2
. A busca sorteia valores aleatórios no intervalo 

[−10,10] e avalia a função para cada um deles, registrando o menor valor encontrado.

✅ Versão Inicial

A versão original utilizava um loop for clássico, que a cada iteração:

gerava um número aleatório;

calculava a função;

comparava com o melhor valor atual;

atualizava as variáveis quando necessário.

Essa abordagem funciona, mas realiza várias operações repetidas dentro do loop, o que aumenta o tempo de execução conforme o número de iterações cresce.

✅ Versão Otimizada

A versão otimizada utiliza duas melhorias:

1. Geração de números com Array.from()

Em vez de sortear valores um por um dentro do loop, todos os números aleatórios são gerados de uma vez só.
Essa operação é mais eficiente porque aproveita otimizações internas da engine JavaScript (V8).

2. Uso de reduce() para encontrar o mínimo

O método reduce() percorre a lista uma única vez, comparando valores e mantendo o melhor resultado.
Ele substitui toda a lógica de comparação manual dentro do loop, tornando o código mais curto, mais legível e mais eficiente.

✅ Por que a versão otimizada é melhor
✔ Menos trabalho dentro do loop

A busca pelo mínimo acontece de forma mais direta e com menos variáveis temporárias.

✔ Usa operações otimizadas nativas

Métodos como Array.from() e reduce() são escritos em C++ dentro da engine JavaScript, sendo mais rápidos que um loop manual.

✔ Código mais curto e menos propenso a erro

O algoritmo fica mais claro, fácil de entender e mais simples de manter.

✔ Mesmo resultado com menos operações

A lógica não muda, mas o caminho até o resultado é mais eficiente.


✅ Complexidade dos Algoritmos

A busca aleatória, tanto na versão original quanto na otimizada, possui complexidade de tempo O(n), pois precisa avaliar a função para cada um dos 
𝑛
n valores sorteados.
Não existe forma de “pular” avaliações — todo número testado precisa ter sua função calculada.

Versão Original

Gera um número aleatório por iteração → O(1)

Calcula a função → O(1)

Compara com o melhor até então → O(1)
Repetido por n iterações:


T(n)=n⋅O(1)=O(n)
Versão Otimizada

Array.from() gera todos os valores → O(n)

reduce() percorre todos os valores para achar o mínimo → O(n)


T(n)=O(n)+O(n)=O(n)

A complexidade permanece a mesma, mas o tempo real de execução diminui porque os métodos nativos são mais eficientes.
