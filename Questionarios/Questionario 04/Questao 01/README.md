A implementação de lista sem ordem definida (UnorderedList), apresentada no livro didático da disciplina, utiliza a abstração de nós para manter os elementos inseridos na estrutura. Por exemplo, a função add é responsável por adicionar um elemento a estrutura. Uma forma de implementar essa função, onde o elemento é adicionado ao início do conjunto de valores, pode ser a seguinte:

```py
def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
```

Já a função remove necessita de uma lógica mais elaborada, já que primeiro o elemento a ser removido precisa ser localizado, ao mesmo tempo em que não se perca a referência do nó anterior ao elemento a ser removido, que deverá ser ligado ao nó posterior ao elemento removido. A implementação dessa função, apresentada pelo livro, é a seguinte:

```py
def remove(self,item):
    current = self.head
    previous = None
    found = False
    while not found:
        if current.getData() == item:
            found = True
        else:
            previous = current
            current = current.getNext()

    if previous == None:
        self.head = current.getNext()
    else:
        previous.setNext(current.getNext())
```

Dada essa implementação, é possível perceber que se esse método for chamado para remover um elemento que não se encontra na estrutura, um erro irá ocorrer. Dessa forma, sua tarefa é, dada a implementação abaixo, consertar a função remove de forma a não incorrer em erros, caso o elemento a ser removido não se encontre na estrutura.
