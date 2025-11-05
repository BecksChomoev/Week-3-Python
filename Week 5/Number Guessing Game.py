from random import randrange

random_number = randrange(1, 100)
print(random_number)
user_attempts = 0
user_attempts_limit = 7

print("Welcome to the Number Guessing Game!")
print("You have to guess the number between 1 and 100. You have 5 attempts to guess the number.")

while user_attempts < user_attempts_limit:
    user_input = int(input("Enter your guess: "))

    if user_input != random_number and user_input < random_number:
        user_attempts += 1
        print("Your guess is low than random number!")
    elif user_input != random_number and user_input > random_number:
        user_attempts += 1
        print("Your guess is higher than random number!")
    elif user_attempts == user_attempts_limit:
        print("I'm sorry, you lost :( Try again later!")
    else:
        print("You won! Congratulations! You guessed the number!")
        break