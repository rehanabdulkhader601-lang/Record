#include<stdio.h>
int main(){
    int isvalid=1;
    int arraysize;
    
      //calling method &  stores returned value 
      //passing 'arraysize';int array_size=arraysize
    while (isvalid == 1)
    {
        int arraysize=read_array_size();
        int validated=validate_array_size(arraysize);
        if (validated == 1){

            break;
        }
        printf("array size is not valid..pls try again:");

}
    int myarray[arraysize];
    for(int i=0;i<=arraysize;i++){

}
}
// read array size from kb
int read_array_size(){
    int size;
    printf("enter the array size[>4]:");
    scanf("%d",&size);
    return size;

}

int validate_array_size(int array_size){
    if(array_size>4){
    return 1;

    }
    return 0;
}
