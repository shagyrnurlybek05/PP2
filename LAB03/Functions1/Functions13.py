import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20. "
          f"Take a guess.")
    number = random.randint(1, 20)
    attempts = 0
    while True:
        guess = int(input())
        attempts += 1
        if guess < number:
            print("Your guess is too low."
                  "Take a guess.")
        elif guess > number:
            print("Your guess is too high."
                  "Take a guess.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
guess_the_number()