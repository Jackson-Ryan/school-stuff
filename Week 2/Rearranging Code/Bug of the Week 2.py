word, vowels = "computer", "aeiou"
count = 0
for letter in word:
    if letter in vowels:
        count = count + 1
print("Vowel count:", count)