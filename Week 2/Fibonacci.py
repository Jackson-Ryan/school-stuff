import sys
sys.set_int_max_str_digits(700) # Maximum of 700 Fibonacci numbers. Set to 0 for unlimited.
amount = int(input("Please enter the amount of Fibonacci numbers to generate: "))
sequence = []
a = 1
b = 1
for i in range(amount):
    sequence.append(a)
    a, b = b, a + b
print(sequence)