def solve(a,b):
    return  a*a + 2 * a*b + b*b
print(solve(2,3))

print((lambda a,b: a*a + 2 * a*b + b*b) (2,3))
print((lambda x: x*x*x )(2))