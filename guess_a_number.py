import random

computer_number = random.randint(1, 100)

while True:
    player_guess = input("Guess the number 1 - 100")

    if not player_guess.isdigit() or int(player_guess) < 1 or int(player_guess) > 100:
        print("Invalid Input! Try again...")
        continue

    player_number = int(player_guess)

    if player_number == computer_number:
        print("You guessed it!")
        break
    elif player_number > computer_number:
        print("Your number is higher than the computer's number. Try again with lower number")
    elif player_number < computer_number:
        print("Your number is lower than the computer's number. Try again with higher number")
