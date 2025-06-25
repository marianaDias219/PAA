texto = ["ABBABABAABBBABABBA", "ABAABBABABAABABABBB", "ABBBAAABAAABABAABA"]

n = len(texto)

padrao = "AABB"

m = len(padrao)

def achaPadrao (texto, n, padrao, m):
  kTextos = []
  kRelevancia = []
  i = 0
  indiceP = 0
  indiceT = 0
  contador = 0
  
  while (i < n):

    tam = len(texto[i])
    
    if (padrao[indiceP] == texto[i][indiceT]):
      indiceP+=1
      indiceT+=1
    else:
        indiceT -= (indiceP-1)
        indiceP = 0
      
    if (indiceP == m):    
      contador+=1
      indiceP = 0
      indiceT-=1

    if (indiceT == tam):
      kTextos.append(contador)
      contador = 0
      indiceP = 0
      indiceT = 0
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

k = achaPadrao(texto, n, padrao, m)   
print(k)
