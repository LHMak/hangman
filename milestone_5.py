import random

word_list = ["strawberry", "grape", "banana", "orange",  "blueberry"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = '_'*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed = "".join((self.word_guessed[:index] + guess + self.word_guessed[index + 1:]))
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        print(self.word_guessed)
        guess = input("Please enter a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives == 0:
            print("You lost!")
            break

        elif game.num_letters > 0:
            game.ask_for_input()

        elif num_lives > 0 and game.num_letters < 1:
            print("You won the game!")
            break

play_game(word_list)
