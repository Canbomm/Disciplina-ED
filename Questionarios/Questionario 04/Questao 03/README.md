Uma tabela de dispersão une a agilidade da RAM com a utilidade de chaves "aleatórias". A bordagem é simples, mapear a chave para um índice do vetor que armazena os elementos. Infelizmente, Murphy está conosco e não é viável considerar um mapeamento perfeito, portanto é preciso lidar com colisões.

Assuma que as chaves são valores inteiros, então a dispersão é trivialmente feita com o operador módulo. Ou seja, numa tabela que comporta 8 elementos, a chave 10 é mapeada para o índice 2, assim como a chave 42. No caso de colisão, o tratamento deve ser uma forma de encadeamento externo, ou seja, os elementos devem ser armazenados em uma estrutura de dados externa à tabela de dispersão.

Faça um programa que, dados o tamanho da tabela e uma sequência de chaves, indique como as informações seriam armazenadas.
