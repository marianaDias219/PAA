#include <stdio.h>
#include <stdlib.h>

int intersecao(int a[], int b[], int c[], int n, int m){
  int tam = n+m, tam2 = n, s = 0, l, k = 0, f;
  int d[tam];

  for (int i = 0; i < n; i++){
    d[i] = a[i];
  }

  for (int j = n; j < tam; j++){
    d[j] = b[k];
    k++;
  }

  for (f = 0; f  < tam; f++){
    for(l = 0; l < s; l++){
      if(d[f] == c[l]) break;
    }if(l == s){
      c[l] = d[f];
      s++;
    }
  }
  return s;
  
}
    

int main (void){
  int a[4] = {9, 8, 6, 4};
  int b[6] = {8, 6, 5, 3, 2, 1};
  int c[10];

  int p = intersecao (a, b, c, 4, 6);
  for (int y = 0; y < p; y++){
    printf("%d  ", c[y]);
  }
}
