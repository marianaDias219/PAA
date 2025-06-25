# Algoritmo Mergesort
# Objetivo: Ordenar lista
# Complexidade: O(n logn)

def mergeSort(vetor):
    i=0
    j=0
    k=0
    if len(vetor) > 1:
        meio = len(vetor)//2
        esquerda = vetor[:meio]
        direita = vetor[meio:]
        mergeSort(esquerda)
        mergeSort(direita)
      
        while i < len(esquerda) and j < len(direita):

            if esquerda[i] < direita[j]:
                vetor[k]=esquerda[i]
                i += 1
            else:
                vetor[k]=direita[j]
                j += 1
            k += 1

        while i < len(esquerda):

            vetor[k]=esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            vetor[k]=direita[j]
            j += 1
            k += 1
    return vetor


a= [4,6,1,2,7,3,1,6,3,7,12,533,76,34,123,51]
mergeSort(a)
print(a)
