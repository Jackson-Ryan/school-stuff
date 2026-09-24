from datetime import datetime
def calculate_fine(days_late, first_offence):
    day = datetime.now().strftime('%A')
    max_fine = 5
    if days_late <= 0:
        fine = 0
    elif first_offence:
        fine = days_late * 0.1
    else:
        fine = days_late * 0.2
    if fine > max_fine and day != "Friday" or day != "Saturday":
        fine = max_fine
    elif day == "Friday" or day == "Saturday":
        fine = fine * 2
        if fine > 10:
            fine = 10
    else:
        fine = fine
    if days_late > 60:
        print("This is a warning, please return the book immediately.")
    return fine

print(calculate_fine(40, False))