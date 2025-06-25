# Algoritmo Quicksort
# Objetivo: ordenar lista
# Complexidade: Pior caso = O(n^2)
  # Caso Médio = O(n logn)
  # Melhor caso = O(n logn)

def particao (x, esq, dir):
  pivo = x[dir]
  i = esq - 1
  
  for j in range (esq, dir):
    if (x[j] < pivo):
      i+=1
      aux = x[i]
      x[i] = x[j]
      x[j] = aux
    
  aux = x[i+1]
  x[i+1] = x[dir]
  x[dir] = aux
  
  return (i+1)


def QSort (x, esq, dir):
  if(esq < dir):
    pos = particao(x, esq, dir)
    QSort(x, esq, pos-1)
    QSort(x, pos+1, dir)



a= [4,6,1,2,7,3,1,6,3,7,12,533,76,34,123,51]
QSort(a, 0, len(a)-1)
print(a)
