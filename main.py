from replit import clear
import random
from hangman_words import word_list
import hangman_art

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print("You already selected this letter... get it together.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Incorrect my friend. You have {lives} lives left.")
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])