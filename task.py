name = input("What's your name? ")
name = name.strip().capitalize()
print("Hi " + name + ", I'm colab!")
print("To get to know you better, it would be amazing if you could tell me a bit about yourself.")
place = input("So " + name + ", where did you grow up? ").strip()
job = input(place + " is amazing! Ok, so what is your dream job? ").strip()
animal = input(job + " sounds so interesting. Finally, what's your favourite animal? ").strip().lower()
animal = animal.removeprefix("a ").removeprefix("an ")
if animal == "puppy" or animal == "dog" or animal == "cat":
  print("That's so cute!")
elif animal == "alligator" or animal == "crocodile" or animal == "spider":
  print("Brrr... I'm scared of those.")
else:
  print("That's an interesting choice!")
print("So to wrap up: you are " + name + ", you grew up in " + place + ", and your dream job is " + job + ". Oh, and your favourite animal is " + animal)