#include <stdio.h>

void mochilaDinamica (int p[], int u[], int n, int m, int *matriz[]){
  int valor1;
  int valor2;
  int j, i, k;
  for(i = 0; i <= n;i++){
     matriz[0][i] = 0;
  }for(j = 1; j <= m;j++){
     matriz[j][0] = 0;
    for (k = 1; k <= n; k++){
      valor1 = matriz[j][k];
      if(p[j-1]>1){
        valor2 = 0;
      }else{
        valor2 = matriz[j-p[k-1]][k-1] + u[k+1];
      }
    }if (valor1 > valor2){
      matriz[j][k] = valor1;
    }else{
      matriz[j][k] = valor2;
    }
  }
}

void imprime(int *matriz[], int m, int n){
  for (int i = 0; i <= m; i++){
    for (int j = 0; j <=n; j++){
      printf("%d", matriz[i][j]);
    }
  }
}



