"""Simple command-line calculator - UCS745 Lab Assignment Q1."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    op = input(f"Enter operation {list(OPERATIONS)}: ").strip()
    b = float(input("Enter second number: "))
    if op not in OPERATIONS:
        print("Unknown operation")
        return
    print("Result:", OPERATIONS[op](a, b))


if __name__ == "__main__":
    main()
