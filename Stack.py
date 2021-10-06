books=[] #stack LIFO
books.append("learn c")
books.append("learn c++")
books.append("learn JAVA")
print(books)


books.pop()
print(books)
print("Now the top book is : ",books[-1])

books.pop()
print(books)
print("Now the top book is : ",books[-1])
books.pop()
print(books)
if not books:
    print("NO BOOK LEFT")
