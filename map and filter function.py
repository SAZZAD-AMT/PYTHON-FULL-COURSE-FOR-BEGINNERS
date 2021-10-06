
#using map
def square (x):
    return x*x

num = [1,2,3,4,5]

result = list(map(square,num))
print(result)

#filtering

even = list (filter(lambda x: x %2==0,num))
print(even)