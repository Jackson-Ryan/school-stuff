marks = [58, 89, 72, 91, 68]
highest_mark = marks[0]

for mark in marks:
    if mark > highest_mark:
        highest_mark = mark

print("The highest mark is:", highest_mark)