<img src="https://i.imgur.com/QmG29Ww.png"  width="300" height="164">

Universidade Privada de Hyakkaou (UPH), uma instituição para os privilegiados com currículo extremamente peculiar, destinada às crianças de proeminentes famílias burguesas de todo o país de Nippon. Não é talento atlético ou intelectualidade que regem o nivelamento dos alunos, é a habilidade de leitura de seu oponente, a arte de negociar. E que maneira de testar e aprimorar essas habilidades, senão um currículo rigoroso em apostas e jogos de azar? Na UPH, os vencedores vivem como reis, e os perdedores são submetidos às mais baixas vidas, mas quando Yumeko é transferida para a universidade, ela ensinará a essas crianças de que, realmente, é feito um grande apostador.

Sendo o representante da classe, coube a você a tarefa de apresentar a universidade a Yumeko, desde as dependências estudantis até o ambiente de apostas, que foi onde ela – impulsivamente – decidiu jogar seu primeiro jogo. A compulsividade em apostar era visível nos olhos dela e, tendo em vista que suas habilidades em apostas inexistem, você decidiu usar sua proficiência em programação para implementar um algoritmo para analisar as chances favoráveis à sua nova amiga.

Um jogo qualquer pode ter seu estado representado como uma estrutura de dados, e podemos, a partir disso, montar uma árvore de jogo que indica, a partir de uma situação inicial (raiz) e definindo quais as possíveis situações subsequentes (galhos), a quais situações terminais pode-se chegar (folhas). Por exemplo, o jogo-da-velha por ser representado por uma matriz 3×3, e partindo do estado inicial desta matriz estar vazia, podemos alterar este estado sucessivas vezes, pela jogada de um "X" ou um "O", até chegar à vitória de um dos jogadores ou ao empate.

<img src="https://i.imgur.com/xzpS4RC.png"  width="400" height="263">

Este tipo de abordagem é muito interessante para ajudar na tomada de decisões, dada uma situação, pode-se verificar quais os resultados possíveis e tentar guiar as escolhas das ações para chegar ao resultado mais desejado. Por exemplo, na seguinte situação o jogador X tem 5 opções de jogada, mas a casa no canto superior esquerdo ou a do meios são as que lhe dão a maior chance de vitória.

<img src="https://i.imgur.com/g2sNf2u.png"  width="60" height="60">

Dada uma árvore de estados, é possível estimar a probabilidade de vencer para cada caminho de forma simples: basta dividir a quantidade de folhas em que se vence pela quantidade total de folhas. Desta forma, você solicitou acesso aos bancos de dados contendo registros de jogos antigos de modo a poder, a partir desses resultados, construir uma árvore de probabilidades que, futuramente, permitiria inferir a quem as chances favoreciam em cada jogo de Yumeko, e analisar como ela decidiu apostar a partir dessas condições. Seu trabalho é, dada uma árvore de jogo, implementar as seguintes funcionalidades:

* gametree: mostra a estrutura da árvore fornecida, usando os caracteres "__" para especificar o nível do nó.
* probtree: mostra a árvore de jogo, onde cada nó tem sua probabilidade de vitória explicitamente definida, usando os caracteres ".." para especificar o nível do nó.

**Entrada**

A entrada consiste em sequências pares de informações $< s,f >$, separadas por espaço. O status s do jogo é um dentre os símbolos $\{V,D,E,?\}$ que indicam, respectivamente, vitória, derrota, empate, e indeterminado; e $f$ é a quantidade de possíveis situações que podem ser alcançadas imediatamente após este estado. É garantido que $0≤f≤100$ e que o status final de um jogo (quando não é possível alcançar uma nova situação) é vitória, derrota ou empate. Em seguida são dadas $f$ linhas, cada uma contendo um par de informações definidas da mesma forma. Ou seja, a primeira linha dá o status de um nó da árvore e as $f$ seguintes os status de cada um de seus nós filhos. Isto ocorre sucessivamente até que toda árvore esteja estruturada. Por fim, é dado um dos comandos definidos, indicando o que se espera como resultado.
