#include <stdio.h>
#include <stdlib.h>

int intersecta(int a[], int b[], int c[], int n, int m){
  int cont = 0, n1 = n, p, tam = n+m, tam2 = n; 
  
  for(int i = 0; i < n; i++){
    c[i] = a[i];
  }
  
   for(int j = 0; j < m; j++){
    for(int f = 0; f < m; f++){
      if(b[j] == c[f]){
        cont++;
    }
  }if(cont == 0){
          c[n1] = b[j];
          n1++;
          tam2++;
        }
  
  cont = 0;
  }

  //Ordena o vetor
  for(int k = 0; k < tam2; k++){
    for (int l = 0; l < tam2 - 1; l++){
      if(c[l] < c[l+1]){
        p = c[l];
        c[l] = c[l+1];
        c[l+1] = p;
      }
    }
  }
  return tam2;
}

int main (void){
  int a[4] = {1, 2, 3, 8};
  int b[6] = {2, 4, 5, 8, 7, 9};
  int c[10];

  int x = intersecta (a, b, c, 4, 6);
  for (int y = 0; y < x; y++){
    printf("%d  ", c[y]);
  }

  

  
}
