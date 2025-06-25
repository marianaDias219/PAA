#include <stdio.h>
#include <stdlib.h>

int parentesis (char* p){
  int cont1 = 0, cont2 = 0, s = sizeof(p), i;
  for (i = 0; i < s; i++){
    if (p[i] == '('){
      cont1++;
    }if (p[i] == ')'){
      cont2++;
    }
  }
  if(cont1 == cont2) return 1;
  else return 0;
}
    

int main (void){
  char* exp = "((2*2))";
  int r = parentesis (exp);
  if(r == 1) printf("CORRETA");
  else printf("INCORRETA");
}
