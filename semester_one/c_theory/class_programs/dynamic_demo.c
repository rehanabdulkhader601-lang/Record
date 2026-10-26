#include<stdio.h>
#include<stdio.h>

int main(){
    int *p;
    p=(int*)malloc(5*sizeof(int));
    printf("%d",p[2]);
    return 1;
}


