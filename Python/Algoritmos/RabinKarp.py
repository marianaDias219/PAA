# Algoritmo RabinKarp
# Objetivo: descobri primeira ocorrência de padrão
# Complexidade: Pior caso = O(n.m)
  #Caso Médio: O(n + m)

d = 256
def rabin_Karp(padrao, texto, numPrimo):
    N = len(texto)
    M = len(padrao)
    j = 0
    p = 0    
    t = 0    
    h = 1
    recorrencia=0
 
    for i in range(M-1):
        h = (h*d)%numPrimo
 
    for i in range(M):
        p = (d*p + ord(padrao[i]))%numPrimo
        t = (d*t + ord(texto[i]))%numPrimo
 
    
    for i in range(N-M+1):
        
        if p==t:
            for j in range(M):
                if texto[i+j] != padrao[j]:
                    break
                else: j+=1
 
            
            if j==M:
                recorrencia+=1
 
        
        if i < N-M:
            t = (d*(t-ord(texto[i])*h) + ord(texto[i+M]))%numPrimo          
            if t < 0:
                t = t+numPrimo
    return recorrencia

b = rabin_Karp("ola", "asbdolasndjbnola", 33325846)
print(b)
