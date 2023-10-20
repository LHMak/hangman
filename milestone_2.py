import random

word_list = ["strawberry", "grape", "banana", "orange", "blueberry"]

word = random.choice(word_list)

print(word)

guess = input("Please enter a letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That's not a valid input.")