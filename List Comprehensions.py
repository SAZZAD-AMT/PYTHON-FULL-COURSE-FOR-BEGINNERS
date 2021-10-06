

num = [1,2,3,4,5]
even = list (map(lambda x: x*x,num))
print(even)


print( [x*x for x in num]) #list comprehention
print([x for x in num if x%2==0])