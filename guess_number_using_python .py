"""
Build a number guessing game — computer picks a random number, user keeps guessing until correct.
* Guess: 50 → Too low! Guess: 75 → Too high! Guess: 63 → 🎉 Correct!

"""

import random
computer_no = random.randint(1, 100)
tries = 0

while True:
    gusse_no = int(input("guess you number between 1 - 100: "))
    tries += 1

    if gusse_no == computer_no:
        print(f"🎉 Congratulation you have succesfully guessed in {tries} tries! 🎉")
        break

    elif gusse_no > computer_no:
        print("Wrong guess! --- Go lower --- ")

    elif gusse_no < computer_no:
        print("Wrong guess! --- Go higher --- ")