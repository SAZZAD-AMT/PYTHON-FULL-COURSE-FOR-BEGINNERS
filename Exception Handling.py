try:
    num = int(input("Enter Number : "))
    result = 10 / num
    print(result)
    print("Done")

except ZeroDivisionError:
    print("ZeroDivisionError")
except IndexError:
    print("Index Error")
finally:
    print("Successful")
