# Hangman

## Table of Contents

## Project description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

I am undertaking this project as part of my journey studying with AiCore. With this, I aim to gain more experience coding in Python and using Github for version control. I intend to update this README after hitting each milestone of the project.

Of note, some things I have learnt are:
- Creating a new class and initialising its attributes.
- Defining class methods and calling them both inside and outside the class.
- General research and debugging issues.
- Committing, pulling and pushing changes to a remote repo.
- Writing a README and the meaning of an MIT license.

## Installation instructions
No installation is required for this project. Just run 'milestone_5.py'

## Usage instructions
The game can be played by running milestone_5.py.

### **Pre-game**
- At the start of the game, a word will be chosen from a predefined list. 
- The player will then be presented with a string of underscores corresponding to the number of characters in the word.

### **Game-loop:**
- The player will then be asked guess a letter in the word by inputting a single alphabetical letter.
- If the letter belongs in the word, its position will be revealed and the player will be asked to guess another letter.
- If the letter does not belong in the word, the player will lose a life.

### **End-game**
- If the player guesses all of the letters in the word, a message will be displayed and the game will end.
- If the player runs out of lives, a message will be displayed and the game will end.


## File structure of the project
milestone_2.py - This script contains the basic code for choosing a word, taking a user's input as a guess and finally checking the chosen word for the presence of the user's guess.

milestone_3.py - This script contains the code from milestone_2.py, tidied up with the introdction of ask_user_input() and check_guess() functions.

milestone_4.py - This script contains the code form milestone_3.py. This time, the Hangman class has been created which initialises attributes such as the chosen word, number of lives the player has and which letters have been guessed. At this stage, most of the functionality of the game is there.

milestone_5.py - This script contains all functionality from previous milestones. In addition, the master function 'play_game()' has been introduced. This function determines the number of lives the player has as well as containing the win/loss conditions of the game. 

## License information
This project is licensed under the terms of the MIT license.
