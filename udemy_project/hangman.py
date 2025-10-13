import random

hang_word = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
print(hang_word)
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ["ardvark", "baboon", "camel"]
lives = 6


chosen_word = random.choice(word_list)
# print(chosen_word)

place_holder = ""
word_length = len(chosen_word)

for position in range(word_length):
    place_holder += "_"
print(place_holder)

game_over = False
correct_letters = [ ]

while not game_over: # Use a while loop to allow the user to keep guessing until they find all the letters in the chosen_word.w
    guess = input("Guess a letter: ").lower()


    display = ""  # Create a display string which contains the letters and underscores
   
    for letter in chosen_word: 
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(HANGMANPICS[6 - lives])

        if lives == 0:
            game_over = True
            print("*************************************** YOU LOSE ***************************************")

    if "_" not in display:
        game_over = True
        print("*************************************** YOU WON ***************************************")

    # print(HANGMANPICS[lives]) # Print the corresponding hangman stage based on the number of lives leftf


