# Beginner-Projects

Project 1: Hello World + User Input Form
## Code
```python

👋 This is the first project in my Python Beginner Projects Series.
It introduces two fundamental concepts in Python programming:

Printing Output (using print())

Taking User Input (using input())

print("Hello, World! 👋")

name = input("What is your name? ")
age = input("How old are you? ")

print("Nice to meet you,", name + "! You are", age, "years old.")
print("Did you know? In 5 years, you will be", int(age) + 5, "years old! 🚀")
Hello, World! 👋
What is your name? Maheen
How old are you? 20
Nice to meet you, Maheem! You are 20 years old.
Did you know? In 5 years, you will be 25 years old! 🚀
## Code
```
# 🧮 Project 2: Simple Python Calculator  
## Code
```python
# 🧮 Project 2: Simple Python Calculator  

## 📌 Description  
This is the **second project** in my **Python Beginner Projects Series**.  
It is a **Simple Calculator** made in Python that performs **basic arithmetic operations**.  

✅ Perfect for beginners who want to learn **user input, conditions, and error handling**.  

---

## ✨ Features  
- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division (with **Zero Division Error Handling**)  
- 🎯 Beginner-friendly and easy to use  

---

## 🛠️ How It Works  
1. The program asks the user to enter **two numbers**.  
2. The user selects an operation (`+`, `-`, `*`, `/`).  
3. The calculator shows the **result** instantly.  
4. If the user tries dividing by **zero**, a warning appears.  

---

## 📸 Example Run  

Welcome to Python Calculator! 🧮
Enter first number: 25
Enter second number: 5
Choose operation (+, -, *, /): /

Result: 5.0
## Code
```
🎲 Project 3: Number Guessing Game

Welcome to Project 4 of the Python Beginner Project Series! 🚀
In this project, we create a fun and interactive Number Guessing Game, where the computer secretly chooses a number and the player has to guess it within limited attempts.

📌 Features

Computer randomly picks a number between 1 and 50

Player has 7 attempts to guess the number

Hints are given: "Too High" ⬆️ or "Too Low" ⬇️

Handles invalid inputs gracefully ⚠️

Fun, beginner-friendly game 🎉

🛠️ Concepts Covered

Python’s random module (random.randint())

Using loops (while) for repeated attempts

Conditionals (if-elif-else) for game logic

Error handling with try-except to catch invalid inputs
## Code
```python
import random

print("🎲 Welcome to the Ultimate Number Guessing Game! 🎲")
print("I'm thinking of a number between 1 and 50...")
print("Can you guess it? Let's find out! 🚀")

# Generate random number
secret_number = random.randint(1, 50)

# Attempts allowed
attempts = 7
print(f"You have {attempts} attempts. Good luck! 🍀\n")

while attempts > 0:
    try:
        guess = int(input("👉 Enter your guess: "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue

    if guess == secret_number:
        print(f"🎉 BOOM! You got it right! The number was {secret_number}. 🏆")
        break
    elif guess < secret_number:
        print("⬆️ Too low! Try a bigger number.")
    else:
        print("⬇️ Too high! Try a smaller number.")

    attempts -= 1
    print(f"❤️ Attempts left: {attempts}\n")

if attempts == 0:
    print(f"😢 Oh no! You're out of attempts. The secret number was {secret_number}. Better luck next time!")
## Code
```
🤝 Contribute

Found a bug or have an idea?
Fork the repo and submit a pull request. Contributions are always welcome!

🎯 Learning Outcomes

How to generate random numbers using Python

Building interactive games with loops

Handling user input errors to make code professional

Applying conditional logic for decision-making

🎮 Project 4: Rock Paper Scissors Game

Welcome to Project 3 of the Python Beginner Project Series! 🚀
In this project, we build a simple Rock, Paper, Scissors Game where the user plays against the computer. This project is great for learning how to handle user input, randomization, and conditional logic in Python.

📌 Features

Play Rock ✊, Paper ✋, or Scissors ✌️ against the computer

Computer move generated using Python’s random module

Handles invalid user input gracefully

Clear winner/loser/draw messages

Fun and beginner-friendly project 🎉

🛠️ Concepts Covered

random.choice() for random computer moves

Getting and validating user input with input() and .lower()

if-elif-else conditions to compare moves

Printing dynamic game results

## Code
```python

import random

print("Welcome to Rock, Paper, Scissor Game")

choices = ["rock", "paper", "scissor"]

user_choice = input("Enter your choice (rock, paper, scissor)").lower()

computer_choice = random.choice(choices)

print("Your choice", user_choice)
print("Computer choice", computer_choice)

if user_choice == computer_choice:
    print("It's a tie")
elif (user_choice == "rock" and computer_choice == "scissor") or \
     (user_choice == "paepr" and computer_choice == "rock")or \
     (user_choice == "scissor" and computer_choice == "paper"):
    print ("You win")
elif user_choice in choices:
    print("Computer wins")
else:
    print("Invalid input! Please choose rock, paper, scissor")
## Code
```

💡 Next Steps

Add a scoring system (best of 3 or best of 5)

Create a loop so the game can be played multiple times

Expand the game to include extra moves like "Lizard" and "Spock" 🦎🖖

🤝 Contribute

Found a bug or want to suggest an improvement?
Feel free to fork the repo and submit a pull request!

🎯 Learning Outcomes

Understand how to use Python’s random module

Learn if-elif-else conditions in a real-world example

Practice handling user input effectively

Build confidence with small but practical coding projects
