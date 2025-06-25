#include <stdio.h>
#include <stdlib.h>


int ordena(int v1[], int v2[], int v3[], int t1, int t2){
  
  int i, j = 0, k = 0, c = 0, l = t1+t2;

  for (i = 0; i < l; i++){
    if(j >= t1 && k <= t2){
      v3[i] = v2[k];
      c++;
      k++;
    }else if(k >= t2 && j <= t1){
      v3[i] = v1[j];
      c++;
      j++;
    }else if (k <= t2 && j <= t1){
      if(v1[j] < v2[k]){
      v3[i] = v1[j];
      c++;
      j++;
    }else if(v1[j] == v2[k]){
      v3[i] = v1[j];
      c++;
      j++;
      k++;
    }else if(v1[j] > v2[k]){
      v3[i] = v2[k];
      c++;
      k++;
    }else{
      break;
    }
    }
  
  }return c;
}

int main (void){
 
  int vetor1[3] = {1, 8, 10};
  int vetor2[4] = {1, 2, 5, 12};
  int vetor3[10];

  int x = ordena(vetor1, vetor2, vetor3, 3, 4);

  for (int a = 0; a < x-1; a++){
    printf("%d", vetor3[a]);
  }
  
}
