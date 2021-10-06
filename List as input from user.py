n=input("Enter the list : ")

num=n.split()
sum=0
for x in num:
    sum=sum+int(x)
print(sum)


numberofword=0
numberofdigit=0
numberofletter=0

text=input("Enter String : ")

for x in text :
    x=x.lower()
    if x>='a' and x<='z':
        numberofletter=numberofletter+1
    elif x>='0' and x<='9':
        numberofdigit=numberofdigit+1
    elif x==' ':
        numberofword=numberofword+1

print("numberofletter : ",numberofletter)
print( "numberofword : ",numberofword+1)
print("numberofdigit : ",numberofdigit)
