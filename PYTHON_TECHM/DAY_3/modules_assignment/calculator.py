# calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"

# Importing and using the calculator module
if __name__ == "__main__":
    from calculator import divide
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", divide(num1, num2))