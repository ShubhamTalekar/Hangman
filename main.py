import random

with open('wordlist.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]

a_e = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter .lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print(" ")
    done = True

    guess = input(f"Allowed Errors left {a_e}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        a_e -= 1
        if a_e == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
if done:
    print(f"Your Found th Word! It was {word}!")
else:
    print(f"Game Over! The Word was {word}!")