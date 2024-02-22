# Guess a Number Game

## Overview

This Python program implements a simple "Guess a Number" game where the player has to guess a randomly generated number within a certain number of tries.

## Instructions

1. Run the program.
2. Enter your first name, last name, and age when prompted.
3. If you are above 4 years old, you will be prompted to start the game.
4. You will have 5 tries to guess the correct number.
5. If you run out of tries, the game ends, revealing the correct number.
6. After each guess, you will be informed whether your guess is higher or lower than the secret number.
7. If you guess the number correctly, you win and have the option to play again.

## Terms of Service

- To play, you must be above 4 years old.

## Usage

```python
python main.py
```

## Functionality

`main()`

- Calls the start_game() function to initiate the game.

`check_age(age)`

- Checks if the player's age is above 4.
- If valid, greets the player and proceeds with the game.
- If invalid, prompts the player to enter a valid age.

`start_game()`

- Prompts the player to enter their age.
- If the age is valid, asks if the player wants to start the game.
- Calls the play_game(answer) function to start the game.

`play_game(answer)`

- Initiates the game based on the player's response.
- Generates a random secret number between 1 and 10.
- Allows the player 5 tries to guess the number.
- Informs the player if the guess is higher or lower than the secret number.
- If the player runs out of tries, reveals the correct number.
- After each game, prompts the player if they want to play again.

`guess_a_number(secret, user_num, num_tries)`

- Compares the player's guess with the secret number.
- Informs the player if their guess is higher or lower than the secret number.
- Tracks the number of tries remaining.
- If the player guesses the correct number, declares victory and offers to play again.

---

> This documentation provides an overview of the game, instructions for usage, terms of service, and explanations of each function's functionality.

