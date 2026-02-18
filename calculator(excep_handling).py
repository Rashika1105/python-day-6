def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            print("Result:", num1 + num2)

        elif choice == '2':
            print("Result:", num1 - num2)

        elif choice == '3':
            print("Result:", num1 * num2)

        elif choice == '4':
            try:
                print("Result:", num1 / num2)
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")

        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except Exception as e:
        print("Unexpected error occurred:", e)

# Run calculator
calculator()
