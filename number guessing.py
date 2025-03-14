import random
from random import randint

print("Welcome to the number guessing game! \nI am thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

def number_guessing_game():
    number = int(randint(1,100))
    if level == "easy":
        attempts = 10
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            attempts -= 1
            if guess > number:
                print("Too high. \nGuess again.")
            elif guess < number:
                print("Too low. \nGuess again.")
            else:
                print("Congrats, you have found it!")
                break
    elif level == "hard":
        attempts = 5
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            attempts -= 1
            if guess > number:
                print("Too high. \nGuess again.")
            elif guess < number:
                print("Too low. \nGuess again.")
            else:
                print("Congrats, you have found it!")
                break

