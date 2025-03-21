import random
from logo import logo
from word_list import word_list
from stages import stages
lives = 6
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
is_Not_Win = True

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

correct_letters = []
while is_Not_Win:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        print("You win")
        is_Not_Win = False
    if guess not in chosen_word:
        print(stages[lives])
        if lives == 0:
            print("You lose")
            break
        lives -= 1
