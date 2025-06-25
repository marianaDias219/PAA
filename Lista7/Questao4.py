import random


def fat (n):
  if (n == 0): return 1
  else: return n*fat(n-1)


def checaPosicao (vetor, tam):
  contador = 0;
  for i in range (0, tam):
    if (vetor[i] == i+1):
      contador = 1
      break
  if (contador == 0): return 1
  else: return 0


def checaVetor (vetor, tam):
  vetorAux = []
  cont = 0
  for i in vetor:
    if(i not in vetorAux):
      vetorAux.append(i)
      cont = cont + 1
  if(cont == tam): 
    if (checaPosicao(vetorAux, cont) == 1): return 1
    else: return 0
  else: return 0


def lasVegas (vetor, tam, fat):
  vetorFinal = []
  i = 0
  while (i < fat):
    vetorAux = []
    for i in range(len(vetor)):
      vetorAux.append(random.choice(vetor))
    if(checaVetor(vetorAux,tam ) == 1 and vetorAux not in vetorFinal):
      vetorFinal.append(vetorAux)
      i = i + 1
  return vetorFinal


v = [1, 2, 3]
tam = len(v)
print(lasVegas(v, tam, fat(tam)))
