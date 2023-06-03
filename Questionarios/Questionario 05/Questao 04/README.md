Na matemática, a Sequência de Fibonacci, é uma sequência de números inteiros, começando por 0, na qual, cada termo subsequente corresponde à soma dos dois anteriores. Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência:

$$0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,⋯$$

Após dominar o uso de funções recursivas envolvendo fibonacci, você ficou com uma pergunta na cabeça: "Quantas vezes cada chamada para a função fibonacci é realizada para cada número menor que n?" Para ajudar a responder a essa pergunta, você tentou uma abordagem mais visual que ficou da seguinte forma:

![Fibonacci](https://i.imgur.com/7Jm20xt.png)

Perceba que ela começa pelo valor que você deseja calcular (Fibonacci de 4). Essa chamada gera outras duas chamadas para Fibonacci de 2 e 3. A chamada de Fibonacci de 2 gera as chamadas de Fibonacci de 1 e 0 enquanto a chamada de Fibonacci de 3 gera as chamadas de Fibonacci de 2 e 1. Por fim, a chamada de Fibonacci de 2 gera as chamadas de Fibonacci de 1 e 0.

Para não precisar sempre desenhando, o nosso professor mestre das artes marciais pediu a sua ajuda para implementar a um programa que conte quantas vezes cada chamada da função fibonacci(n) é realizada, para cada valor de entrada diferente da função fibonacci(n) é chamada em sua implementação recursiva.
