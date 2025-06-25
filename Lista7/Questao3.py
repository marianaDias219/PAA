def alocacaoPessoas (v, vetor, tam, i, j, soma, vetfinal):
  if(j == tam):
    if(i == tam): return vetFinal
    else:
      j = 0
      i = i+1

  vetorAux = vetor
  vetorAux[i] = v[i][j]
  somaAux = 0
  
  for k in (vetor):
    somaAux = somaAux + vetorAux[k];
  if(soma > somaAux): 
    soma = somaAux
    vetFinal.append(vetorAux)
    
  alocacaoPessoas (v, vetorAux, tam, i, j+1, soma, vetfinal)


def checaVetor(vetor, tam):
  vetorAux = []
  cont = 0
  for i in vetor:
    if(i not in vetorAux):
      vetorAux.append(i)
      cont = cont + 1
  if(cont == tam): return 1
  else: return 0


def calculaMinimo (vetor, tam):
  vetMin = []
  menorNum = vetor[0][0]
  menorInd = 0
  for i in range (0, tam):
    for j in range (0, tam):
      if (vetor[i][j] < menorNum):
        menorNum = vetor[i][j]
        menorInd = j
    vetMin.append(menorInd)
    menorNum = vetor[i][0]
  return vetMin

v = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8],[7, 6, 9, 4]]
n = len(v)
print(calculaMinimo (v, n))
vetFinal = []
alocacaoPessoas (v, n, 0, 0, 0, vetFinal)
