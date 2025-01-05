import random

def guess_the_secret_number():
    """
    This app allows the user to guess the secret number.
    The app responds with 'cold' or 'hot' based on proximity to the secret number.
    It counts the number of attempts until the correct number is guessed.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    previous_difference = None

    print("Guess the secret number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        difference = abs(secret_number - guess)

        if guess == secret_number:
            print(f"Congratulations! You've found the secret number {secret_number} in {attempts} attempts.")
            break
        elif previous_difference is None:
            if difference <= 10:
                print("Hot!")
            else:
                print("Cold!")
        else:
            if difference < previous_difference:
                print("Getting hotter!")
            else:
                print("Getting colder!")
        
        previous_difference = difference

if __name__ == "__main__":
    guess_the_secret_number()
