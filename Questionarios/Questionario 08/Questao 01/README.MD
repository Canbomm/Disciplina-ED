No desenvolvimento de um programa que usa árvores, pode ser necessário ou útil a visualização da estrutura. Considere uma árvore em que cada item é definido pela seguinte classe Arvore:

```py
class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []
```

Defina a função mostra que recebe como argumento a raiz de uma árvore e um prefixo, e mostra todos os elementos da árvore, com sua hierarquia claramente definida no formato especificado. Assuma que todo elemento presente no atributo filhos de um item é também uma Árvore.
