Uma árvore binária  é uma variação da estrutura de dados árvore em que cada nó, além de armazenar um dado, pode ter até duas subárvores. Neste problema, ela é definida na classe ArvoreBinaria que tem como atributos um dado e as subárvores esq e dir. Defina a função rotaciona_direita que recebe como argumentos a raiz de uma árvore e returna a árvore rotacionada à direita.

A rotação à direita é simples, supondo uma árvore qualquer, trata-se de modificar a estrutura da árvore substituindo a raiz pela raiz da subárvore à esquerda. Como é uma reestruturação dos elementos, a raiz removida deve ser mantida na árvore, tornando-se a raiz da subárvore à direita e tendo como subárvore à esquerda a subárvore à direita da nova raiz. Graficamente, este processo torna o nó amarelo a nova raiz da árvore:

!['Representação de uma rotação árvore binária'](https://i.imgur.com/0JCsc1C.png 'Rotação árvore binária')
