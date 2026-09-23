def biggest_of_three(a, b, c):
    if a >= b and a >= c:
        biggest = a
    elif b >= a and b >= c:
        biggest = b
    else:
        biggest = c
    return biggest

result = biggest_of_three(4, 9, 6)
print("Biggest: ", result)