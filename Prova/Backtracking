#include <stdio.h>

int checaPosicao (int vetor[], int tam){
  int contador = 0;
  for (int i = 0; i < tam; i++){
    if (vetor[i] == i+1){
      contador = 1;
      break;
    }
  }
  if (contador == 0) return 1;
  else return 0;
}

void troca(int vetor[], int i, int j){
	int aux = vetor[i];
	vetor[i] = vetor[j];
	vetor[j] = aux;
}

void permuta(int vetor[], int inf, int sup, int tam){
	if(inf == sup){
    if (checaPosicao (vetor, tam) == 1){
		for(int i = 0; i <= sup; i++)
			printf("%d ", vetor[i]); 
		printf("\n");
    }
	}
	else{
		for(int i = inf; i <= sup; i++){
			troca(vetor, inf, i);
			permuta(vetor, inf + 1, sup, tam);
			troca(vetor, inf, i); //backtracking
		}
	}
}

int main(int argc, char *argv[]){
	int v[] = {1, 2, 3};
	int tam_v = sizeof(v) / sizeof(int);
	permuta(v, 0, tam_v - 1, tam_v);

	return 0;
}
