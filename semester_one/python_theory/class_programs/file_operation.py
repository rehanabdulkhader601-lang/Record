file=open("simple_file.txt","r",encoding="utf-8")
content=file.read()
print(content)
print("-"*25)
content=file.readline()

file.seek(0)       #bring the file pointer to the begining of the file
content=file.readline()
print(content.strip())
content=file.readline()
print(content)
print("_"*30)
file.close()   #closes the file

file=open("simple_file.txt","w",encoding="utf-8")
file.write("\nAbcd")        #writting
file.close()
