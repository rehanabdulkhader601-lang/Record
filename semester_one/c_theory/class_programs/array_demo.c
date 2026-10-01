//pgm to store and display 5 subject marks
//for student
#include<stdio.h>
int main(){
    int my_marks[5];                      //integer array of size 5
    int sub_marks[5];     //declares an array 'sub_marks'
    // with SIZE 5 'int' type 
    //storing dat/array initialization - array_name[index]=data/value;
    sub_marks[0]=80;  // stores '80' in an array position while index is '0'
    sub_marks[1]=78;
    sub_marks[2]=68;
    sub_marks[3]=58;
    sub_marks[4]=88;
    //fetch first array element from 'sub_marks'
    //dynamic initialization of 'my_marks'
    printf("enter first number:[int data]");
    scanf("%d",my_marks[0]);
    printf("enter second subject marks:[int data]");  
    scanf("%d",my_marks[1]);   
    printf("enter third subject marks:[int data]");  
    scanf("%d",my_marks[2]);   
    printf("enter fourth subject marks:[int data]");  
    scanf("%d",my_marks[3]);   
    printf("enter fifth subject marks:[int data]");  
    scanf("%d",my_marks[4]);
    
    printf("first subject marks: %d",my_marks[0]);
    printf("second subject marks: %d",my_marks[1]);
    printf("third subject marks: %d",my_marks[2]);
    printf("fourth subject marks: %d",my_marks[3]);
    printf("fifth subject marks: %d",my_marks[4]);

    for (int i=0;i<5;i++){
        printf("enter the first subject marks:");
        scanf("%d",&my_marks[0]);
        printf("enter the second subject marks:");
        scanf("%d",&my_marks[1]);
        printf("enter the third subject marks:");
        scanf("%d",&my_marks[2]);
        printf("enter the fourth subject marks:");
        scanf("%d",&my_marks[3]);
        printf("enter the fifth subject marks:");
        scanf("%d",&my_marks[4]);
}
}