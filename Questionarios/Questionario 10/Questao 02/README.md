O saudoso Mussum seria uma webcelebridade nos dias atuais, mas provavelmente não teria muito traquejo tecnológico para encontrar seus amigos na rede social. Depois de aceitar os pedidos de conhecidos, ele reparou que faltavam muitos, e pediu sua ajuda. 

Dado um grafo descrevendo as relações da rede social, crie um programa que apresente, em ordem alfabética, os prováveis amigos do Mussum. Para encontrar os prováveis amigos de Mussum, considere a seguinte regra: duas pessoas não conectadas que têm pelo menos 3 amigos em comum têm alta probabilidade de serem amigos entre si e portanto, são prováveis amigos. 

**Entrada**

A primeira linha da entrada indica quantos são os n vértices do grafo (1≤n≤100). As n linhas seguintes representam, cada uma, a informação de um vértice no formato: $id,A,v1,v2,⋯,vA,$ onde id é um string identificando o vértice, A é a quantidade de arestas ligadas a este vértice, e cada $vi \neq id$ é um string identificando um vértice adjacente a id. O primeiro id é sempre o do Mussum.