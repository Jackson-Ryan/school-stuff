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

option = int(input("Please enter your selection:" \
"1. Print Header" \
"2. Hrs to Mins conversion" \
"3. Is Number even?" \
"4. BMI Calculation"))
if option == 1:
    subject = input("Input your subject: ")
    print_header(subject)
elif option == 2:
    num = input("Input the amount of time in hours: ")
    convert_to_minutes(num)
elif option == 3:
    weight = input("Input your weight in KG: ")
    height = input("Input your hight in metres: ")
    bmi(weight, height)