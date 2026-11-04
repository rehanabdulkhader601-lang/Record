#include <stdio.h>
int main(){
    int n;
    int size;
    //take array size from the user 
    printf("Enter size of an array:");
    scanf("%d",&size);
    //declare an array
    int a[size];

    //take array elements from the user
     for (int i=0; i<size;i++)
     {
        printf("enter array element%d:",i+1);
        scanf("%d",&a[i]);
     }

     //bubble sort logic
     for (int i=0;i<size;i++)
     {
        for(int j=0;j<size -i;j++)
        {
            if(a[j]>a[j+1])
            {
                int temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
     }
     // display array elements
     printf("array elements are :");
     for (int i=0;i<size;i++)
     {
        printf("\n%d",a[i]);
     }
     return 0;
}