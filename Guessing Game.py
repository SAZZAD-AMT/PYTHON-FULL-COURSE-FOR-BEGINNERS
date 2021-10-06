from random import randint
for x in range (1,6):
    gussnumber = int(input("Enter value in 5 : "))
    randomnumber = randint(1,5)

    if gussnumber == randomnumber:
        print("You Have WON")

    else:
        print("you Have LOst")
        print("The random number is : ", randomnumber)

