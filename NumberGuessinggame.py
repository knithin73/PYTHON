import random
import logo
import os
os.system('clear')
print(logo.logo)
print("Welcome to the number Guessing Game! \n I'm thinking of a number between 1 and 100 \n")
random_number=random.randint(1,100)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard' : ")
if difficulty=="easy":
    attempts=10
else:
    attempts=5


print(f"You have {attempts} attempts remaining to guess the number ")


for i in range(attempts):
    guess = int(input("Make a guess : "))
    if guess==random_number:
        print(f"Congratulations! You guessed correctly. {random_number}")
        
    elif guess<random_number:
        print("Your guess is TOO LOW")
        attempts-=1
        if attempts>0:
            print(f"\nGuess again\nYou have {attempts} attempts remaining to guess the number")
        else:
            print("You have ranout of guesses,you lose")
        
    elif guess>random_number:
        print("Your guess is TOO HIGH\nGuess again\n")
        attempts-=1
        if attempts>0:
            print(f"\nGuess again\nYou have {attempts} attempts remaining to guess the number")
        else:
            print("You have ranout of guesses,you lose")
