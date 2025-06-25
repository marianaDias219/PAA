# Algoritmo kWayMerge
# Objetivo: organizar grande volume de dados
# Complexidade: O(n logk)
n = 4 ;
 
# Função merge
def merge(esq, dir, saida) :
     
    # para armazenar o ponto de início dos vetores esquerda e direita
    vetorEsquerda = esq
    vetorDireita = ((esq + dir) // 2 + 1)
 
    # para armazenar o tamanho do vetor 
    tamEsq = ((esq + dir) // 2 - esq + 1)
    tamDir = (dir - (esq + dir) // 2)
 
    # vetor temporário para armazenar os vetores esquerda e direita
    vetTempEsq = [0] * tamEsq
    vetTempDir = [0] * tamDir
 
    # armazenando os dados no vetor esquerdo
    for i in range(0, tamEsq) :
        vetTempEsq[i] = saida[vetorEsquerda + i]
 
    #  armazenando os dados no vetor direito
    for i in range(0, tamDir) :
        vetTempDir[i] = saida[vetorDireita + i];

    # armazenar o atual endereço dos vetores temporários
    esqAtual = 0
    dirAtual = 0;
 
    # to store the current index
    # for output array
    in1 = vetorEsquerda;
 
    # two pointer merge for two sorted arrays
    while (esqAtual + dirAtual < tamEsq + tamDir) :
        if (dirAtual == tamDir or (esqAtual != tamEsq and
            vetTempEsq[esqAtual] < vetTempDir[dirAtual])) :
            saida[in1] = vetTempEsq[esqAtual];
            esqAtual += 1; in1 += 1;
        else :
            saida[in1] = vetTempDir[dirAtual];
            dirAtual += 1; in1 += 1;
 
# Code to drive merge-sort and
# create recursion tree
def divide(esq, dir, saida, vetor) :
     
    if (esq == dir) :
 
        # base step to initialize the output
        # array before performing merge
        # operation
        for i in range(0, k) :
            saida[esq + i] = vetor[esq];
        return;
     
    # to sort left half
    divide(esq, (esq + dir) // 2, saida, vetor);
 
    # to sort right half
    divide((esq + dir) // 2 + 1, dir, saida, vetor);
 
    # merge the left and right half
    merge(esq, dir, saida);
 
# Driver code
if __name__ == "__main__" :
 
    # input 2D-array
    vetor = [5, 2, 1, 7, 3, 15, 18]
  
    # Number of arrays
    k = len(vetor);
     
    # Output array
    saida = [0] * (k);
     
    divide(0, k, saida, vetor);
     
    # Print merged array
    for i in range(0, k) :
        print(saida[i]);
