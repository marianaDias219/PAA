a = "DISCIPLINA"
b = "ISCA"

n = len(a)
m = len(b)

def subsequencia2 (a ,n, b, m):

  indiceA = n-1
  indiceB = m-1
  contador = 0
  contadorIndice = 0
  i = n

  while(i > 0):
    
    if(a[indiceA] == b[indiceB]):
      contadorIndice += indiceA
      indiceA -= 1
      indiceB -= 1
      contador += 1
    else:
      if(contador > 0):
        indiceA -= 1
      else:
        indiceA -= 1
        indiceB = m-1
    if(contador == m):
      print(contadorIndice)
      break
    
subsequencia2 (a ,n, b, m)
