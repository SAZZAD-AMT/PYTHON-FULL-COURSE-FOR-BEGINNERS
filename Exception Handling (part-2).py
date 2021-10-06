
try:
    num1 = int(input("Enter 1st NUM : "))
    num2 = int(input("Enter 2st NUM : "))
    num =num1/num2
    print(num)

except (ZeroDivisionError,ValueError):
    print("Insert incorrect Number.")

finally:
    print("THANKS...")


