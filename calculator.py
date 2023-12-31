#define functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

#define calculator application 
def calculator():
    while True:
        print("===== Simple Calculator =====")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice in ('1', '2', '3', '4','5'):
            if choice == '1':
                result = add(num1, num2)
                operator = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operator = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operator = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operator = '/'
            else:
                print("Exiting the calculator")
                break
                
            
            print(f"{num1} {operator} {num2} = {result}")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the calculator
calculator()

