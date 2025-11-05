from random import randrange

random_number = randrange(1, 100)
user_attempts = 0
user_attempts_limit = 7

print("Welcome to the Number Guessing Game!")
print("You have to guess the number between 1 and 100. You have 7 attempts to guess the number.")

while user_attempts < user_attempts_limit:
    user_input = int(input("Enter your guess: "))

    if user_input == random_number:
        print("You won! Congratulations! You guessed the number!")
        break
    elif user_input < random_number:
        user_attempts += 1
        print("Your guess is lower than the random number!")
    else:
        user_attempts += 1
        print("Your guess is higher than the random number!")
else:
    print(f"You lost! The number was {random_number}. Try again!")