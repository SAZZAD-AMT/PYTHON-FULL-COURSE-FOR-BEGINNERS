#xxargs //truples

def student(*details):
    print(details[2])


student(101,"SAZZAD",2.66)


def add(*number):
    sum=0
    for x in number :
        sum=sum+x
    print(sum)

add(10,20)
add(20,40,70,50)

#xxxargs //dictionaray

def stu (**det):
    print(det)

stu(ID =2019,NAME = "SAZZAD")