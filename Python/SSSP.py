'''
->  Single Source Shortest Path

n nós
m vértices bidirecionais
-> depois de visitar todos os nós pelo menos uma vez ele para
-> menor sequência de nós
-> entrada: n m
    posição das arestas bidirecionais
'''

#recebendo o número de nós(n) e vértices(m)
entrada1 = input()
formatEntrada1 = entrada1.split(' ')
formatEntrada1 = formatEntrada1
n = int(formatEntrada1[0])
m = int(formatEntrada1[1])

#recebendo os vértices em um vetor
vertices = [[]]

for i in range (m):
  entrada2 = input()
  formatEntrada2 = entrada2.split(' ')
  vertices.append(int(formatEntrada2[0]))
  vertices.append(int(formatEntrada2[1]))

vertices.pop(0)
print(vertices)

#construindo a sequencia
seq = []
seq.append(vertices(0))
vertices.pop(0)
seq.append(vertices(1))
no = vertices(1)
vertices.pop(1)

while len(seq) < n:
  indice = vertice.index(no)
  seq.append(indice+1)


  
