while True:
    print("Mini calculator:")
    number_1 = int(input("Enter Valur-1:"))
    number_2 = int(input("Enter value-2:"))
    op = input("Enter the operator(+,-,/,*):")
    if op == "+":
        print(number_1 + number_2)
    elif op == "-":
        print(number_1 - number_2)
    elif op == "/":
        print(number_1 / number_2)
    elif op == "*":
        print(number_1 * number_2)
    elif op == "e":
        exit()
    else:
        print("The is something went wrong")
