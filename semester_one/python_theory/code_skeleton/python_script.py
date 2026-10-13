#you need to provide students data as follows:name,phonenumber,email,5 subject marks and get the total 
#must be implemented using nested list.
name=input("enter your name:")
rollno=int(input("enter student rollno:"))
phonenumber=int(input("enter your phone number:"))
email=input("enter your email:")
sub1=int(input("enter sub1 marks:"))
sub2=int(input("enter sub1 marks:"))
sub3=int(input("enter sub1 marks:"))
sub4=int(input("enter sub1 marks:"))
sub5=int(input("enter sub1 marks:"))

list=int(input("enter the number of list:"))
sub_marks=[]

sub_marks.append(name)
sub_marks.append(rollno)
sub_marks.append(phonenumber)
sub_marks.append(email)
sub_marks.append(sub1)
sub_marks.append(sub2)
sub_marks.append(sub3)
sub_marks.append(sub4)
sub_marks.append(sub5)
print(sub_marks)
