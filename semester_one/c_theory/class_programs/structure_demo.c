#include <stdio.h>
// structure defination
struct student{
    // structure members: ID,name,contactno and pin are the structure members
    int id;
    char name[10];
    char contactno[15];
    int pin;
};
int main(){
    // creating structure variable "firststudent" of type "student"
    struct student firststudent;
    struct student secondstudent;
    firststudent.id=100; 
    secondstudent.id=200;
    firststudent.pin=10;
    secondstudent.pin=20;
    printf("first studentid %d",firststudent.id);
    printf("second studentid %d",secondstudent.id);
    printf("first pin %d",firststudent.pin);
    printf("second pin %d",secondstudent.pin);
    
}
