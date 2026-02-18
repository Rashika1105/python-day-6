try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
except ValueError:
    print("Try only numericals for age")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))