file=open("student.txt","r+")
#print(file.read())
#print(file.readable())
#print(file.writable())

#text=file.read()
#print(text)
#size= len(text)
#print(size)

test=file.readlines()[0]
print(test)

file.close()