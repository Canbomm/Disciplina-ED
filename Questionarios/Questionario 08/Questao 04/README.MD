## Não consegui essa ##

Uma árvore AVL é uma forma de organizar uma árvore binária de modo que esteja sempre balanceada. Para isso, usa uma informação muito simples, para cada nó ela calcula a diferença d entre as alturas de suas subárvores. Para um no R de filhos RE (a esquerda) e RD (a direita), essa diferença é:

$$d(R)=altura(RE)−altura(RD)$$

Dada uma árvore binária, calcule essas diferenças e apresente a árvore.

| Input                                               | Expected                                                  |
|-----------------------------------------------------|-----------------------------------------------------------|
| (a (b () ()) (c () ()))                             | (0 (0 () ()) (0 () ()))                                   |
| (a (b (d () ()) (e () ())) (c (f () ()) (g () ()))) | (0 (0 (0 () ()) (0 () ())) (0 (0 () ()) (0 () ())))       |
| (a () (b () (c (d () ()) ())))                      | (-3 () (-2 () (1 (0 () ()) ())))                          |
| (a () ())                                           | (0 () ())                                                 |
| (a (b (c (d (e (f (g () ()) ()) ()) ()) ()) ()) ()) | (6 (5 (4 (3 (2 (1 (0 () ()) ()) ()) ()) ()) ()) ())       |
| (a () (b () (c () (d () (e () (f () (g () ()))))))) | (-6 () (-5 () (-4 () (-3 () (-2 () (-1 () (0 () ()))))))) |
