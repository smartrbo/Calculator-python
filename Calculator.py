def calculator():
    first_number=float(input("Enter the first number:"))
    second_number=float(input("Enter the second number:"))
    operator=input("Enter the opretors:")

    if operator == "+":
        cal=first_number + second_number
    elif operator == "-":
        cal=first_number - second_number
    elif operator == "*":
        cal=first_number*second_number
    elif operator == "/":
        cal = first_number/second_number
    elif operator == "%":
        cal=first_number%second_number
    else:
        print("Invalid operator")
        return
    print("The Result is:", cal)

calculator()

