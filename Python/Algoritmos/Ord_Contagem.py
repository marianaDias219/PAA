# Algoritmo Ordenação por Contagem
# Objetivo: Ordena lista (espaço extra)
# Complexidade: O(k+n)

def contagem (a, n):
  #encontrar maior elemento do vetor
  maior = a[0]
  for i in range(1, n):
    if (maior < a[i]): maior = a[i]

  #criação do vetor para computar a frequencia dos elementos
  c = [0]*(maior+1) 
  
  for i in range(0, n):
    c[a[i]] += 1

  for i in range (1, len(c)):
    c[i] += c[i-1]

  b = [0]*(n) 
  
  for i in range (n-1, -1, -1):
    b[c[a[i]]-1] = a[i]
    c[a[i]] -= 1

  return b

#teste
a = [4,6,1,2,7,3,1,6,3,7]
b = contagem (a, len(a))
print(b)
