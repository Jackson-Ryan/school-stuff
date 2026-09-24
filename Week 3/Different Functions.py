def print_header(subject):
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸")
    print("--------", subject, "---------")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸")
def convert_to_minutes(hours):
    mins = hours * 60
    return mins
def is_even(number):
    if number % 2 == 1:
        print("The number is odd")
    else:
        print("The number is even")
def bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m^2)
    bmi = round(bmi, 1)
    return bmi

option = int(input("Please enter your selection: \n 1. Print Header \n 2. Hrs to Mins conversion \n 3. Is Number even? \n 4. BMI Calculation \n"))
if option == 1:
    subject = input("Input your subject: ")
    print_header(subject)
elif option == 2:
    num = int(input("Input the amount of time in hours: "))
    print("The amount of time in minutes is: ", convert_to_minutes(num))
elif option == 3:
    number = int(input("Input a number: "))
    is_even(number)
elif option == 4:
    weight = int(input("Input your weight in kg: "))
    height = int(input("Input your height in m: "))
    print("Your BMI is: ", bmi(weight, height))
else:
    print("Invalid selection")