# Simple Calculator Program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Choose an operation (1-5): ")

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == "1":
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Error! Please enter valid numbers.")
        elif choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    calculator()
