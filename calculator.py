# Calculator CLI App

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def main():
    print("Welcome to Command-Line Calculator")

    while True:
        print("\nSelect an operation:")
        print(" + : Addition")
        print(" - : Subtraction")
        print(" * : Multiplication")
        print(" / : Division")
        print(" q : Quit")

        operator = input("Enter operator (+, -, *, /, q to quit): ")

        if operator == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if operator not in ('+', '-', '*', '/'):
            print("Invalid operator! Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)

            print("Result:", result)
        except ValueError:
            print("Error: Invalid number input! Please enter valid numbers.")

if __name__ == "__main__":
    main()



############################################################################################



