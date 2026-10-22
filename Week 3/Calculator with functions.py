import re


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def calculate(equation):
    """Calculate an equation containing two numbers and one operator."""
    match = re.fullmatch(
        r"\s*([-+]?(?:\d+(?:\.\d*)?|\.\d+))\s*([+\-*/])\s*"
        r"([-+]?(?:\d+(?:\.\d*)?|\.\d+))\s*",
        equation,
    )

    if match is None:
        raise ValueError("Please use the format number operator number.")

    num1, operator, num2 = match.groups()
    num1 = float(num1)
    num2 = float(num2)

    if operator == "+":
        return addition(num1, num2)
    if operator == "-":
        return subtraction(num1, num2)
    if operator == "*":
        return multiplication(num1, num2)
    if num2 == 0:
        raise ZeroDivisionError("You cannot divide by zero.")
    return division(num1, num2)


equation = input(
    "Please enter an equation (for example, 1 + 2): "
)

try:
    answer = calculate(equation)
    print(f"Answer: {answer:g}")
except (ValueError, ZeroDivisionError) as error:
    print(f"Error: {error}")
