
from math import *

n=int(input("Enter NUmber : "))


sum =0
for x in range(1,n+1,1):
    sum=sum + pow(x,x)
print(sum)