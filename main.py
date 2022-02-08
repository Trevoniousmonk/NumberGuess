import random
from art import logo
print(logo)

chosen_number = int(0)

if chosen_number == 0:
  chosen_number = chosen_number =+ random.randint(1,100)

print("Welcome to NumberGuess!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  attempts = 10
else:
  attempts = 5

game_over = False
while game_over == False:
  print("Guess again.")
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))

  if guess == chosen_number:
    print(f"You got it! The answer was {chosen_number}.")
    game_over = True
  elif guess < chosen_number:
    print("Too low.")
    attempts -= 1
  elif guess > chosen_number:
    print("Too high.")
    attempts -= 1
  if attempts == 0:
    game_over = True
    print("You've run out of guesses, you lose.")
