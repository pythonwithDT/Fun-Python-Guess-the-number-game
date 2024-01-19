## Let's go through the code step by step:

User Input:

<div>
Copy code
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
</div>
The user is prompted to input their first and last names.

Function Definition:

python
Copy code
def check_age(age):
    if 5 <= age <= 20:
        print(f"Hello {first_name} {last_name}. Let's play a guess game")
    else:
        print("Invalid age")
        exit()
A function check_age is defined, which checks if the entered age is between 5 and 20. If not, it prints an error message and exits the program.