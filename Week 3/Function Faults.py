def add_bonus(score):
    return score + bonus
    bonus = 10

print(add_bonus(50))
print(bonus) # bonus is a locally defined variable. To print here, it would need to be a global variable.