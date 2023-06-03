## Nao consegui essa ##

Durante a suas missões de mercenário, a comando de Greff Carga, você resgatou um item chamado Óðrerir. O único problema é que ao tentar acessar o dispositivo, você percebeu que ele possui uma tecnologia acoplada que exige uma execução meticulosa de alguns comandos para destravá-lo. Infelizmente, faz parte da sua missão conseguir esse acesso. 

<img src="https://i.imgur.com/etQXn6J.gif" alt="Painel" width="300"/>

Pra sua sorte, debaixo do dispositivo há uma lista de instruções que dita o seguinte: "O painel encontra-se atualmente no número X. Para abrir o dispositivo, com menos de 20 ações, deve-se operar as instruções disponíveis (incrementar, dobrar ou inverter) para transformar o número X no número Y. Após as ações, pode-se, uma única vez, tentar destravar o dispositivo. Caso o painel não contenha o número Y no momento em que a ação destravar seja executada, o dispositivo não poderá mais ser aberto e se autodestruirá.".

Para não correr o risco de destruir o Óðrerir, você deve escrever uma função chamada destravarPainel, para te auxiliar a executar o número mínimo de operações para destravar o artefato e recuperar o seu valioso conteúdo.

**Entrada**

Não há entrada de dados, a função é chamada para valores arbitrários definidos nos casos de teste. Essa função recebe como entrada três parâmetros:

* painel: Um objeto para manipular o artefato.
* origem: Inteiro com o valor inicial no painel.
* objetivo: Inteiro com o valor no qual o dispositivo poderá ser destravado. 

O objeto painel, possui os seguintes métodos de acesso ao dispositivo: 

* verificaPainel(): rotina que retorna um inteiro com o valor atual no painel. Não consome ações.
* verificaAcoesRestantes(): rotina que retorna um inteiro com o número restante de ações disponíveis. Não consome ações.
* incrementarValor(): rotina que incrementa em uma unidade o valor do painel. Retorna True caso haja ações suficientes e a modificação ocorra com sucesso ou imprime uma mensagem de erro e retorna  é False, caso contrário. É garantido que, em nenhum momento, o valor irá ultrapassar 99999.
* dobrarValor(): rotina que dobra o valor (multiplica por 2) do painel. Retorna True caso haja ações suficientes e a modificação ocorra com sucesso ou imprime uma mensagem de erro e retorna  é False , caso contrário. É garantido que, em nenhum momento, o valor irá ultrapassar 99999.
* inverterValor(): rotina que inverte o valor do painel. Retorna True caso haja ações suficientes e a modificação ocorra com sucesso ou imprime uma mensagem de erro e retorna  é False, caso contrário. Essa rotina desconsidera zeros a esquerda, ao realizar a inversão.
* abrirArtefato(): rotina que verifica, uma única vez, se o valor do painel corresponde ao valor do objetivo. Retorna uma string com o conteúdo do artefato, caso este tenha sido aberto com sucesso ou imprime uma mensagem de erro e retorna None caso contrário .