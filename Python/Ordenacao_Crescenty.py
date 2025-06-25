#receber entradas, separar por meio do ";" e ordenar de maneira crescente pelo tamanho dos elementos
'''
entrada = input()
formatEntrada = entrada.split(';')
entrada = sorted(formatEntrada, reverse = False)
entrada.pop(0)
print(entrada)

nComp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
tam = len(entrada)

for i in range (tam):
  app = entrada[i][0]
  qnt = entrada[i][1]

  for j in range (qnt):
'''

# n vértices numerado (ai)
# inicialmente não existem arestas
# adicionar aresta -> pagar : custo = ai+aj
# oferta m = (x, y, w,)
'''
input: n m
       a1, a2, a3, ...
       valores de m
'''

# formando matriz com os pesos das arestas e matriz de ofertas

entrada = input()
formatEntrada = entrada.split(' ')
n = formatEntrada[0]
m = formatEntrada[1]

vertices = input()
formatVertices = vertices.split(' ')
matrizVertices = [([0]*n) for i in range(n)]
for i in range (n):
  for j in range (n):
      if (i == j):continue
      elif (i > j):continue
      else: 
        matrizVertices[i][j] = (formatVertices[i]+formatVertices[j])
        matrizVertices[j][i] =  (formatVertices[i]+formatVertices[j])
  

matrizOfertas = [[0 for x in range(0,m)] for i in range (0,m)]
for i in range(m):
  ofertas = input()
  formatOfertas = ofertas.split(' ')
  matrizOfertas[formatOfertas[0]-1][formatOfertas[1]-1] = matrizOfertas[formatOfertas[0]-1][formatOfertas[1]-1] + formatOfertas[2]
  matrizOfertas[formatOfertas[1]-1][formatOfertas[0]-1] = matrizOfertas[formatOfertas[1]-1][formatOfertas[0]-1] + formatOfertas[2]

# percorrer a matriz de pesos comparando com a matriz de ofertas
# para escolher o menor valor

print(matrizVertices)
print(matrizOfertas)


