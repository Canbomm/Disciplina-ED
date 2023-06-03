Um grafo G = (V, A) armazena as informações de um conjunto de vértices e outro de arestas. Defina a classe Grafo que implementa essa estrutura de dados e algumas funcionalidades.

A classe Grafo deve ter os atributos vertices, que armazena a informação dos vértices e outro arestas, que armazena as relações entre eles. Estes atributos devem ser implementados como o tipo list, tuple ou dict. Cada vértice é definido por um par (id,dado), identificando o vértice e a informação armazenada nele, respectivamente. Cada aresta é definida por um par (ido,idd), identificando os ids dos vértices de origem e destino, respectivamente. A classe deve fornecer os seguintes métodos:

* insere_v(id, dado), que insere um vértice com as informações dadas.
* insere_a(id_o, id_d), que insere uma nova aresta com as informações dadas.
* remove_v(id), que remove o vértice com o id dado, se existir (a remoção de um vértice implica na remoção de todas as arestas relacionadas a ele).
* remove_a(id_o, id_d), que remove uma nova aresta dada, se existir.
* grau_saida, que recebe o id de um vértice e retorna o grau de saída dele, se existir, 0 caso contrário.
* grau_entrada, que recebe o id de um vértice e retornar o grau de entrada dele, se existir, 0 caso contrário.
* alcancavel, que recebe os ids de dois vértices u,v e retorna um booleano indicando se o vértice v pode ser alcançado a partir de u.

Os métodos de alteração da estrutura serão chamados para executar uma das instruções, como a seguir:

* IV A dado_A insere o vértice com id==A e a informação dadoA no grafo;
* IA A B insere uma aresta do vértice de id==A para o vértice de id==B, se ambos existirem;
* RV A remove o vértice de id==A, se existir, e todas as arestas relacionadas a ele; e
* RA A B remove a aresta do vértice de id==A para o vértice de id==B, se existir.

Os outros métodos listados serão chamados nos testes.

** Entrada ** 

Não há leitura de dados, isso é feito automaticamente. A entrada consiste de uma linha contendo o número 0≤n≤100 indicando a quantidade de operações sobre o grafo, seguida de n linhas contendo, cada uma, uma instrução conforme as previstas.
