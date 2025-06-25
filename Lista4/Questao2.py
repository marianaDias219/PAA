texto = ["AABBABABAABBBABABBABAABBABAABAB"]
padroes = "AABB"

n = len(texto)
m = len(padroes)

def achaPadrao(texto, n, padroes, m):

  q = 3354393
  d = 64
  dM = 0
  t0 = 0
  h = d^(m-1) % q
  
  for i  in range (0, m):
    dM = (d*dM + padroes) % q
  h1 = 0
  for i in range (0, m):
    (h1*d + index(padroes[i])) % q 
  h2 = 0
  for i in range (0, m):
    (h2*d + index(texto[i])) % q
  i = 1
  while (h1 != h2 and (i <=n-m)):
    h2 = (h2 + d*q - index(texto[i]*dM)) % q
    h2 = (h2*d + index(texto[i+m])) % q
  return i+1

k = achaPadrao(texto, n, padroes, m)
print(k)
