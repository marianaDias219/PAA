
texto = ["AAB BABB ABBBAB AAAB", "AB AABB ABAB BAABBB ABBB", "ABBB A AAABB ABBA BAABA"]

n = len(texto)

padrao = "AABB"

m = len(padrao)

def achaPadrao2 (texto, n, padrao, m):
  kTextos = []
  kRelevancia = []
  i = 0
  indiceP = m-1
  indiceT = m-1
  contador = 0
  
  while (i < n):

    tam = len(texto[i])

    if(texto[i][indiceT] == ' '):
      indiceP = m-1
      indiceT += m
    
    if (padrao[indiceP] == texto[i][indiceT]):
      indiceP -= 1
      indiceT -= 1
    else:
        indiceT = indiceT + (m-indiceP)
        indiceP = m-1

    if(indiceP < 0):
      contador += 1 
      indiceP = m-1
      indiceT = indiceT + (m+1)


    if(indiceT >= tam):
      kTextos.append(contador)
      indiceP = m-1
      indiceT = m-1
      contador = 0
      i+=1
      
  maior = kTextos[0]
  indiceMaior = 0

  for i in range(1, n):
    if (kTextos[i] >= maior):
        indiceMaior = i
        maior = kTextos[i]

  kRelevancia.append(indiceMaior)

  for i in range(0, n):
    if (i != indiceMaior):
      if (kTextos[i] == maior): 
          kRelevancia.append(i)
    else: pass
      
  return kRelevancia

k = achaPadrao2(texto, n, padrao, m)  
print(k)
