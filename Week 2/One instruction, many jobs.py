from fractions import Fraction
temp_c = 0
temp_f = 0
option = input("Enter option 1 for CISC instruction or 2 for RISC style: ")

if option == "1":
    # CISC instruction doing several jobs at once
    # Prediction: I predict that with temp_c = 35, the output will be True because 35 degrees Celsius is equivalent to 95 degrees Fahrenheit, which is greater than 86 degrees Fahrenheit.
    temp_c = Fraction(35)
    is_hot = (temp_c * 9 / 5 + 32) > 86
    print(f"The temperature in Fahrenheit is {(temp_c * 9 / 5 + 32)} and it is hot: {is_hot}")
elif option == "2":
    # RISC style
    temp_c = 35
    temp_f = temp_c * 9 / 5
    temp_f = temp_f + 32
    is_hot = temp_f > 86
    print(f"The temperature in Fahrenheit is {temp_f} and it is hot: {is_hot}")
else:
    print("Invalid option")