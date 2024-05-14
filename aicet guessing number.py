import random

def number_guessing_game():
    name = input("May I ask you for your name?\n ")
    print(f"Hello, {name}!  we are going to play a game. I am thinking of a number between 1 and 200 \n Go ahead. Guess!")

    # Generate a random number between 1 and 200
    secret_number = random.randint(1, 200)
    attempts = 0

    while True:
        guess = input("Guess:")

        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations, {name}! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("The guess of the number that you have entered is too low \nTry Again!")
        else:
            print("The guess of the number that you have entered is too high \nTry Again!")

if __name__ == "__main__":
    number_guessing_game()
