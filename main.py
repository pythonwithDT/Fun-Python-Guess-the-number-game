import random

print("""
========================

Welcome to Guess a Number

========================

In this game, you would guess a number in 5 tries.

You lose if you run out of tries.

Terms of Service:
To play you have to be above 4 years old.
""")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


def main():
    start_game()


def check_age(age):
    if age >= 5:
        print(f"Hello {first_name} {last_name}. lets play 'Guess a number'")
        return True
    else:
        return False


def start_game():
    while True:
        age = int(input("Enter your age: "))
        if check_age(age):
            ready_to_play = input("Do you want to play? [Y/n]: ")
            play_game(ready_to_play)
            break
        else:
            print("Please enter a valid age")


def play_game(answer):
    if answer.lower() == "n":
        exit()
    else:
        secret_num = random.randint(1, 10)
        num_of_tries = 5
        while num_of_tries > 0:
            user_num = int(input("Guess a number between 1 and 10: "))
            if user_num in range(1, 11):
                if guess_a_number(secret_num, user_num, num_of_tries):
                    break
            else:
                print("Enter a number between 1 and 10.")
            num_of_tries -= 1
        else:
            print("You ran out of tries. The correct number was", secret_num)


def guess_a_number(secret, user_num, num_tries):
    if user_num != secret:
        print(f"You have {num_tries - 1} number of tries left")
        if user_num > secret:
            print("Your guess is higher than the number in my mind")
        else:
            print("Your guess is lower than the number in my mind")
        return False
    else:
        print("You won!!!")
        print(f"It took you {6 - num_tries} number of tries")
        continue_play = input("Do you want to play again? [Y/n] ")
        play_game(continue_play)
        return True


main()
