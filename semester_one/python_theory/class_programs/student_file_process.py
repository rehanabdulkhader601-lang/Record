from os import write


with open("students_details.txt","r",encoding="utf-8") as f:
    for line in f:
        total=sum([int(mark) for mark in line.strip().split()[3:1]])
        rollno=line.strip().split()[0]
        firstname=line.strip().split()[1]
        lastname=line.strip().split()[2]
        name=firstname+" "+lastname
        student_list.append(rollno+" "+name+" "+str(total) + "\n")
        print(f"{rollno}\t{name}\t{total}")

        with open("output.txt","a",encoding="utf-8") as wp:
            wp.write(rollno + " " +name+" "+str(total)+"\n")
            
