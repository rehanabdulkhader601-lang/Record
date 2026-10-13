marks=["sachin",50,55,67,76,89]  #declares an list 'marks' to store marks of 'sachin's
my_marks=[]
# dynamic initialization
for number in range(5):
    newmarks=int(input("enter the marks:"))
    my_marks.append(newmarks)


print("list elements are:")
for i in range(len(my_marks)):
    print(my_marks[i])
    