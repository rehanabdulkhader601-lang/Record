#include<stdio.h>
int main(){
    char name[6];
    printf("enter your name:");
    scanf("%19s",name);
    printf("hello, %|\n",name);
    return 0;

    char second[30];
    printf("enter your firstname:");
    fgets(name,sizeof(name),stdin);
    printf("name: %10s",name);
    return 0;
}