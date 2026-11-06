file=open("simple_file.txt","r",encoding="utf-8")
content=file.read()
print(content)
print("."*25)
content=file.readlines()\

file.seek(0)  #string the file pointer to the beginning of the file
content=file.readlines()
print(content.strip())
content=file.readlines()
print(content)
print("_"*25)
file.close()  #closes the file

file=open("simple_file.txt","r",encoding="utf-8")
file.write("\nabcd")        #writing
file.close()  
