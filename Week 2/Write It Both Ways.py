num = int(input("Please enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
elif num % 3 == 0:
    print(f"{num} is divisible by 3.")
elif num % 5 == 0:
    print(f"{num} is divisible by 5.")
else:
    print(f"{num} is not divisible by 3 or 5.")