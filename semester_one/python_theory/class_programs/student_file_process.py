student_list=[]
with open("student_details.txt","r",encoding="utf-8")as f:
    for line in f:
        total=(sum([int(mark) for mark in line.strip().split()[3::]]))  #converting list into int
        
        rollno=line.strip().split()[0] #to get output of rollno,name and total 
        firstname=line.strip().split()[1]
        secondname=line.strip().split()[2]
        name=firstname+" "+secondname
        student_list.append(rollno+" "+name+" "+str(total)+"\n")
print(student_list)
        

with open("output.txt","w",encoding="utf-8")as file:
    file.writelines(student_list)
