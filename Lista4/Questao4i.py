a = "DISCIPLINA"
b = "ISCA"
#b = "IDA"

n = len(a)
m = len(b)

def subsequencia (a ,n, b, m):

  indiceA = 0
  indiceB = 0
  contador = 0
  i = 0

  while(i <= n):
    
    if(a[indiceA] == b[indiceB]):
      indiceA += 1
      indiceB += 1
      contador += 1
    else:
      if(contador > 0):
        indiceA += 1
      else:
        indiceA += 1
        indiceB = 0
    if(contador == m):
      print("SIM")
      break
    if(indiceA == n):
      print("NÃO")
      break

subsequencia (a ,n, b, m)
