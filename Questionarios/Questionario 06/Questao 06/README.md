Seu Anacleto trabalha em uma empresa de assessoria jurídica e ficou incomodado com a displicência dos funcionários responsáveis pela organização dos processos recém-impressos. Ele percebeu que os funcionários colocam os processos em uma pequena mesa (A), um sobre o outro, ignorando a ordem em que são impressos.

Quando consegue um tempinho entre suas tarefas, Seu Anacleto se dirige à essa mesa para ordenar os processos apropriadamente, isto é, de forma crescente, com o processo de maior identificador sobre a mesa e o de menor identificador sobre todos os demais. Ele limpa outra mesa (B), idêntica à mesa A e que fica bem ao lado desta, e começa um cuidadoso procedimento para ordenar os processos:

1. Seu Anacleto pega o processo que está acima de todos os demais.

2. Em seguida, ele pega o próximo processo que está na mesa A, e compara com que está na sua mão: o de menor identificador vai para a mesa B, e o outro permanece em sua mão.

3. Ele repete este processo até que a mesa A esteja vazia e o processo de maior identificador esteja em sua mão.

4. Ele então coloca o processo de sua mão na mesa A e, em seguida, retira processo por processo da mesa B e retorna-os para a mesa A, sempre preservando a ordem, até que a mesa B fique vazia.

5. Caso os processos não fiquem ordenados, ele reiniciará um ciclo deste processo, com o intuito de encontrar o processo com o segundo maior identificador.

6. Para manter a ordenação dos processos na mesa A, Seu Anacleto sempre manterá, no k-ésimo ciclo, os k−1 processos identificados anteriormente intocados sobre a mesa A.

Os funcionários da assessoria jurídica observam Seu Anacleto e ficam curiosos sobre a eficácia do procedimento de ordenação adotado. Mate esta curiosidade desenvolvendo um programa que determina a quantidade mínima de ciclos que Seu Anacleto gastará para ordenar todos os processos na mesa A.

Entrada
A primeira linha da entrada contém um número inteiro N (1≤N≤104), que descreve a quantidade de processos que estão na mesa A.

A segunda linha descreve N inteiros distintos pi (1≤pi≤N), separados por um espaço em branco, representando os identificadores dos processos.

Os valores pi são dados na entrada na mesma ordem em que os processos foram colocados, um sobre o outro, na mesa A pelos funcionários.