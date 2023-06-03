Um grafo G = (V, A) armazena as informações de um conjunto de vértices e outro de arestas. O grau  de um vértice é a quantidade de arestas incidentes nele. O Grau de um grafo é o valor máximo do grau de seus vértices. O "D(grau)" é a ideia inversa, o valor mínimo do grau dos vértices. Faça um programa que receba uma série e instruções e as processe para gerar um grafo não direcionado.

* IV A insere o vértice com id==A no grafo;
* IA A B insere uma aresta do vértice de id==A para o vértice de id==B, se os vértices existirem;
* RV A remove o vértice de id==A, se existir, e todas as arestas relacionadas a ele; e
* RA A B remove a aresta do vértice de id==A para o vértice de id==B, se existir;

**Entrada**

A entrada consiste de uma linha contendo o número 0≤n≤100 indicando a quantidade de operações sobre o grafo, seguida de n linhas contendo, cada uma, uma instrução conforme as apresentadas. Todo id é um string de não mais de 10 caracteres.