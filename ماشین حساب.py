def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
print("Select operation.")

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

def cal():
    choice = input("Enter choice(1/2/3/4): ")
tuple_num = ('1', '2', '3', '4')

    if choice in tuple_num:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
  if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid Input")
cal()
