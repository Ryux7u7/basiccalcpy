print("Basic Calculator")

print("WARNING: Use . instead of , (1.2 + 3.54)")

while True:
    print("What action would you like to do?")
    print("1. +")
    print("2. -")
    print("3. x")
    print("4. /")
    print("0. Quit")

    selection = int(input())

    if selection == 0:
        break

    num1 = float(input("First value: "))
    num2 = float(input("Second value: "))

    if selection == 1:
        rslt = num1 + num2
        print("Result: ", rslt)
    elif selection == 2:
        rslt = num1 - num2
        print("Result: ", rslt)
    elif selection == 3:
        rslt = num1 * num2
        print("Result: ", rslt)
    elif selection == 4:
        if num2 == 0:
            print("A value cannot be divided by zero!")
        else:
            rslt = num1 / num2
            print("Result: ", rslt)
    else:
        print("Please enter a valid option number!\n")