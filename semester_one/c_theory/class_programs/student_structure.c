#include <stdio.h>
struct student{
    int rollno;
    char name[10];
    int marks[3];
    int total;     // to store total marks
    float average;    // to store average marks


};

// method to initialise 5 students
void initialize_student(){
    struct student student_list[5];
    for (int i=0;i<5;i++){
        printf("enter %d the student date",i+1);
        printf("enter student roll number");
        scanf("%d",&student_list[i].rollno);
        printf("enter student name:");
        scanf("%s",&student_list[i].name);
        // to collect 3 subject mark
        for(int j=0;j<3;j++){
            printf("enter %d subject mark:");
            scanf("%d",&student_list[i].marks[j]);
            
        };
    }
int get_total();
    for (int i=0;i<5;i++){
        student_list[i].total=student_list[i].marks[0]+student_list[i].marks[1]+student_list[i].marks[2];
    }
}
float get_average(){
    for (int i=0;i<5;i++){
        student_list[i].average= (float)student_list[i].total/3;
    } 
}

int main(){
    // array of structure
    initialize_student();
    get_total();
    get_average();
    printf("rollno\t\tname\t\tsub_mark\t\t");
    display_students();
    
}


