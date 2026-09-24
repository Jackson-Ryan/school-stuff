marks = [58, 89, 72, 91, 68]
highest_mark = marks[0]
lowest_mark = marks[0]

above_70 = 0
for mark in marks:
    if mark > 70:
        above_70 = above_70 + 1
    if mark > highest_mark:
        highest_mark = mark
    elif mark < lowest_mark:
        lowest_mark = mark
    if mark >= 75:
        print(mark, "is a Distinction.")
    elif mark >= 60:
        print(mark, "is a Merit.")
    elif mark >= 45:
        print(mark, "is a Pass.")
    elif mark < 45:
        print(mark, "is a Fail.")
    else:
        print(mark, "is an Invalid mark.")
    

print("The highest mark is:", highest_mark)
print("The lowest mark is:", lowest_mark)