
# Let's go through the code step by step:

### User Input:

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
```
The user is prompted to input their first and last names.

### Function Definition:

```python
def check_age(age):
    if 5 <= age <= 20:
        print(f"Hello {first_name} {last_name}. Let's play a guess game")
    else:
        print("Invalid age")
        exit()
```
A function check_age is defined, which checks if the entered age is between 5 and 20. If not, it prints an error message and exits the program.

### Age Input Handling:

```python
while True:
    age_num = input("Enter your age: ")
    try:
        age = int(age_num)
        check_age(age)
        break
    except ValueError:
        print("Invalid age. Please enter a valid age")
```
A loop continues until a valid age is entered. The entered age is converted to an integer. If a non-integer value is entered, a ValueError is caught, and the user is prompted to enter a valid age.

### Answer Input Handling:

```python
answer = input("Enter your answer: ")
if answer.lower() == "no":
    exit()
else:
    print("I will think of a number, and you have to guess it")
```
The user is prompted to enter an answer. If the answer is "no" (case insensitive), the program exits. Otherwise, it proceeds to the guessing game.

### Number Guessing Game:

```python
while True:
    guess = True
    while guess:
        num = input("Type a number: ")
        if num == "quit":
            print("Thanks for playing")
            exit()
        print("Thanks for playing")
        if num.isdigit():
            print("Cool!")
            num = int(num)
            guess = False
        else:
            print("Invalid input! Try Again!")
```
A loop runs for the number guessing game. The user is prompted to type a number. If "quit" is typed, the program exits. If a valid number is entered, it proceeds to generate a random secret number and starts the guessing loop.

### Guessing Loop:

```python
secret = random.randint(1, num)

tries = None
count = 1

while tries != secret:
    tries = input("Please type the guess between 1 and " + str(num) + ": ")
    if tries.isdigit():
        tries = int(tries)

    if tries == secret:
        print("You Won")
    else:
        print("Please try again!")
        count += 1
```
Inside this loop, the program generates a random secret number between 1 and the entered number. The user is prompted to guess the number. If the guessed number is correct, the user wins; otherwise, they are prompted to try again.

### Print Result:

```python
print("It took you", count, 'tries')
```
Finally, the program prints the number of tries it took for the user to guess the correct number.

The code combines user input, functions, loops, and conditional statements to create a simple guessing game based on the user's age.
