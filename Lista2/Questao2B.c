#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

//Estrutura da lista de pessoas influentes (nome, quantidade de amigos)
typedef struct {
    char *nome[30];
    int amigos;
} tupla;

static struct { char nome[30]; int amigos; } lista[10];
static int tamanhoLista = 0;

void merge(int i, int m, int f){
    int a, b, c, d;
    int *numeros;
    char *nomes[10];
    numeros = malloc((f - i) * sizeof (int));
    a = i;
    b = m;
    c = 0;
    while(a < m && b < f){
        if(lista[a].amigos <= lista[b].amigos){
            numeros[c++] = lista[a++].amigos;
        }else{
            numeros[c++] = lista[b++].amigos;
        }
    }
    while (a < m){
        numeros[c++] = lista[a++].amigos;
    }
    while (b < f){
        numeros[c++] = lista[b++].amigos;
    }
    for(d = i; d < f; ++d){
        lista[d].amigos = numeros[d-i];
    }
    free(numeros);
}

void mergeSort (int inicio, int final){
    int q;
    if (inicio < final-1){
        q = floor(inicio+final)/2;
        mergeSort (inicio, q);
        mergeSort (q, final);
        merge(inicio, q, final);
    }
}

static void adicionaPessoa(char *n, int a) {
    strcpy(lista[tamanhoLista].nome, n); //Copia as informações de entrada para uma tupla
    lista[tamanhoLista++].amigos = a;  
}

int main(void) {

    adicionaPessoa("Ana", 4);
    adicionaPessoa("Luis", 2);
    adicionaPessoa("Maria", 34);
    adicionaPessoa("João",12);
    adicionaPessoa("Vitoria", 1);

    mergeSort(0, tamanhoLista); 

    for(int k = 0; k < tamanhoLista; k++){
        printf(" %d \n", lista[k].amigos);
    }

}
