import random

date = ["yesterday", "a few years ago", "a long time ago"]
animals = ["a rabbit that lived in germany", "an elephant that lived in germany", "a turtle that lived in germany"]
actions = ["go to the school", "he have a lot of friends", "go university and write the book"]

date = random.choice(date)
animals = random.choice(animals)
actions = random.choice(actions)

print(f"{date} , {animals} and {actions}.")