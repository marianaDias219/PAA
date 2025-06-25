#Algoritmo busca binária
#Objetivo: encontrar o índice de um número
#Complexidade: T(n) = T(n/2) + c => II caso no método mestre
  #O(log n)

def buscaBinaria (vetor, inicio, fim, x):
  if (fim >= inicio):
    meio = (fim+inicio)//2

    if(vetor[meio]== x): return meio
    elif (vetor[meio] > x): return buscaBinaria (vetor, inicio, meio-1, x)
    else: return buscaBinaria (vetor, meio+1, fim, x)

  else: return -1

a = [1,5,7,10,12,16]
num = 7
resp = buscaBinaria (a, 0, len(a)-1, num)
print(resp)
