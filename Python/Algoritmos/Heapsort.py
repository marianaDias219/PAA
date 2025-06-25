#Algoritmo Heapsort
#Objetivo: Montar um heap com os elementos e ordem decrescente
#Complexidade: Montar Heap = O(n)
  #maxHeapify = O(log n)
  #heapsort = O(n logn)

import math

def maxHeapify (a, i, n):
  e = 2*i + 1
  d = 2*i + 2
  maior = i

  if(e < n and a[e] > a[i]): maior = e
  else: maior = i

  if (d < n and a[d] > a[maior]): maior = d

  if(maior != i):
    aux = a[i]
    a[i] = a[maior]
    a[maior] = aux

    maxHeapify (a, maior, n)


def montaMaxHeap (a, n):
  x = math.floor(n/2) - 1
  for i in range (x, -1, -1):
    maxHeapify (a, i, n)


def heapSort (a, n):
  montaMaxHeap(a, n)
  tam = n
  for i in range (n-1, -1, -1):
    aux = a[0]
    a[0] = a[i]
    a[i] = aux
    tam -= 1
    maxHeapify(a, 0, tam)

a = [4,6,1,2,7,3,1,6,3,7,12,533,76,34,123,51]
heapSort (a, len(a)-1)
print(a)
