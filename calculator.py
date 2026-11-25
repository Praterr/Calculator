"""Simple command-line calculator - UCS745 Lab Assignment Q1."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulus by zero is not allowed")
    return a % b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": modulus,
}


def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    op = input(f"Enter operation {list(OPERATIONS)}: ").strip()
    b = float(input("Enter second number: "))
    if op not in OPERATIONS:
        print("Unknown operation")
        return
    try:
        print("Result:", OPERATIONS[op](a, b))
    except ZeroDivisionError as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
