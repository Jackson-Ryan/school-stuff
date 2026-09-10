name = input("What is your name? ")
name = name.capitalize()

while True:
    number = int(input("Hi " + name + ", my name is codey! I can do many things, so to get started, please pick an option from the list below: \n1. Get the time and date\n2. Play a game\n3. access the calculator\n4. Exit\n"))

    if number == 1:
        import datetime
        now = datetime.datetime.now()
        print("The current date and time is: ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
    elif number == 2:
        import random

        secret_number = random.randint(1, 10)
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == secret_number:
            print("Well done, you guessed correctly!")
        else:
            print("Not quite. The number was " + str(secret_number) + ".")
    elif number == 3:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                print("You cannot divide by zero.")
            else:
                result = first_number / second_number
        else:
            print("That is not a valid operator.")

        if operator in ["+", "-", "*"] or (operator == "/" and second_number != 0):
            print("The answer is " + str(result))
    elif number == 4:
        print("Goodbye, " + name + "!")
        break
    else:
        print("That is not a valid option.")
