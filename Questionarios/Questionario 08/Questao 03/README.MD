O Modelo de Objeto de Documento (DOM) fornece uma representação estruturada do documento como uma árvore, é o padrão para HTML, XML e SVG. A ideia é simples, a hierarquia é definida nos níveis, e cada nó tem uma informação que o identifica e outras que apresentam seus atributos.

Neste contexto, considere que cada nó é implementado como um dicionário, ou seja, tem a seguinte estrutura: nos = {'id': {'text' : ?, 'class': ?, 'children': ?}}. A chave id é sempre um string identificando o elemento, e o objeto armazenado é um dicionário contendo as informações como o texto do objeto (string), sua classe (string) e seus nós filhos (dicionário com a mesma estrutura do nó pai).

Defina a função getElementByClassName que recebe a raiz de um DOM e  a(s) class(es) desejadas e retorna uma lista contendo toda chave do nó cuja classe é fornecida. No caso de múltiplas classes, estas são fornecidas separadas por espaço. Considere que a busca não é sensível à caixa.
