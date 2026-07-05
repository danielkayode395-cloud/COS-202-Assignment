print("=" * 50)
print("       MATHEMATICAL CALCULATOR")
print("=" * 50)

while True:

    print("\nChoose Any Operation")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("\\  Floor Division")
    print("^  Exponential")
    print("%  Modulus")
    print("C  Clear")
    print("OFF  Exit")

    sign = input("\nOperation: ").upper()

    match sign:

        case "OFF":
            print("\nSystem Closed Successfully.")
            break

        case "C":
            print("\nCalculator Reset.")

        case "+" | "-" | "*" | "/" | "\\" | "^" | "%":

            left = float(input("First Number: "))
            right = float(input("Second Number: "))

            match sign:

                case "+":
                    value = left + right

                case "-":
                    value = left - right

                case "*":
                    value = left * right

                case "/":
                    if right == 0:
                        print("Cannot divide by zero.")
                        continue
                    value = left / right

                case "\\":
                    if right == 0:
                        print("Cannot divide by zero.")
                        continue
                    value = left // right

                case "^":
                    value = left ** right

                case "%":
                    if right == 0:
                        print("Cannot divide by zero.")
                        continue
                    value = left % right

            print("\nResult:", value)

        case _:
            print("\nPlease enter a valid operation.")