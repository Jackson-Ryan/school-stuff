marks = [[24, 37, 45, 56, 67, 78], [56, 45, 34, 23, 12, 21], [34, 45, 56, 67, 78, 89]]
distinction_count = 0
merit_count = 0
pass_count = 0
fail_count = 0

for row in marks:
    for mark in row:
        if mark >= 75:
            distinction_count = distinction_count + 1
        elif mark >= 60:
            merit_count = merit_count + 1
        elif mark >= 45:
            pass_count = pass_count + 1
        elif mark < 45:
            fail_count = fail_count + 1
        else:
            print(mark, "is an Invalid mark.")

print("Distinction count:", distinction_count)
print("Merit count:", merit_count)
print("Pass count:", pass_count)
print("Fail count:", fail_count)