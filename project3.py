import random

print("Welcone to the ultimate Guessing Number Game")
print("I am thinking of a number between 1 and 50")
print("Can you guess it? Let's Find out")

secret_number = random.randint(1, 50)

attempts = 7
print(f"You have {attempts} attempts. Good luck! \n")

while attempts > 0:
    try:
        guess = int(input("Enter your guess"))
    except ValueError:
        print("Please Enter a valid number!")

        continue

    if guess == secret_number:
        print(f"BOOM!You got it right! The number was{secret_number}")
        break
    elif guess < secret_number:
        print("Too low! Try a bigger number")
    else:
        print("Too high! Try a smaller number")

        attempts -= 1
        print(f"Attempts left {attempts}\n")

if attempts == 0:
    print("Oh no! You are out of attempts,"
          f"The secre number was {secret_number}. Better luck next time ")