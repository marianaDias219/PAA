texto = "CABCCBACBACAB"
padrao = "ABHBABAHC"

n = len(texto)
m = len(padrao)

def cacaterFaltante (texto, n, padrao, m):

  indiceT = 0
  indiceP = 0
  indiceAux = 0
  contadorH1 = 0
  contadorH2 = 0
  i == 1
  
  while (i > 0)
    indiceT = indiceAux
    if (texto[indiceT] == padrao[indiceP])

      indiceT += 1
      indiceP += 1
      
    else:
      if (indiceP == 'H'):
        contadorH1 += 1
        while(padrao[indiceP+1] != texto[indiceT+1]):
          indiceT += 1
          if (padrao[indiceP+1] == texto[indiceT+1]): 
            contadorH2 +=1 
            indiceT = indiceT+2
            indiceP = indiceP+2
      else:
        indiceT += 1

  if(indiceT == n and contadorH1 == contadorH2):
    print("SIM")
    break
  else: 
    print("NÃO")
    break

cacaterFaltante (texto, n, padrao, m)
