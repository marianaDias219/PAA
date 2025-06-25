#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Estrutura da lista de pessoas influentes (nome, quantidade de amigos)
typedef struct {
    char nome[30];
    int amigos;
} tupla;

static struct { char nome[30]; int amigos; } lista[10];
static int tamanhoLista = 0;

//Adicionar pessoas na lista
static void adicionaPessoa(char *n, int a) {
    strcpy(lista[tamanhoLista].nome, n); //Copia as informações de entrada para uma tupla
    lista[tamanhoLista++].amigos = a;  
}

//Retira pessoas da lista
static void deletaPessoa(char *n) {
    int cont = 0;
    while (cont < tamanhoLista) {
        if (strcmp(n, lista[cont].nome) == 0) break;
        ++cont;
    }
    if (cont == tamanhoLista) return;

    printf("%s -> %d amigos\n", n, lista[cont].amigos);
    
    if (cont != tamanhoLista - 1) {
        strcpy(lista[cont].nome, lista[tamanhoLista - 1].nome);
        lista[cont].amigos = lista[tamanhoLista - 1].amigos;
    }
    --tamanhoLista;
}

//Função para exibir os nomes da lista em ordem decrescente de número de amigos
void comparaAmigos(){
  char *maiorT;
  int i, k, maiorNum = 0;
  
  for(k = tamanhoLista; k > 0; k--){        //Verifica qual pessoa tem o maior número de amigos
    for(i = 0; i < tamanhoLista; i++){    
      if (lista[i].amigos > maiorNum){
        maiorNum = lista[i].amigos;
        maiorT = lista[i].nome;
        }
    }
  deletaPessoa(maiorT);                     
  maiorNum = 0;
  }
}

int main(void) {

    adicionaPessoa("Ana", 68452);
    adicionaPessoa("Luis", 75005);
    adicionaPessoa("Maria", 89547);
    adicionaPessoa("João", 99584);
    adicionaPessoa("Vitoria", 105898);

    comparaAmigos();

}
