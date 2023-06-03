Uma característica de muitos programas de transferência de arquivo é a FALTA de precisão para estimar o tempo remanescente de transferência (exemplo aleatório). Num sistema operacional de verdade, o tempo de transferência é estimado com base na taxa de transferência em segundos dos bytes e no número de bytes que restam para serem transferidos. 

A ideia é simples, basta estimar o tempo restante assumindo que a taxa de transferência será mantida para os bytes que ainda não foram enviados. Implemente um patch para realizar esta tarefa adequadamente.
