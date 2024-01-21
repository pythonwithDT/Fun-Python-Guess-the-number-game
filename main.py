import random

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


def check_age(age):
    if 5 <= age <= 20:
        print(f"Hello{first_name}{last_name}. lest play a guess game")
    else:
        print("Invalid age")
        exit()
  
  
while True:
      age_num = input("Enter your age: ")
      try:
          age = int(age_num)
          check_age(age)
          break
      except ValueError:
          print("Invalid age. Please enter a valid age")
          

answer = input("Enter your answer: ")
if answer.lower() == "no":
    exit()
else:
    print("I will think of a number, and you have to guess it")
    
while True:
    guess = True
    while guess:
        num = input("Type a number: ")
        if num == "quit":
            print("Thanks for playing")
            exit()
            
        if num.isdigit():
            print("Cool!")
            num = int(num)
            guess = False
        else:
            print("Incalid input! Try Again")
            

    secret = random.randit(1,num)
 
    tries = None
    count = 1
 
    while tries != secret:
        tries = input("Please type the guess between 1 and" + str(num) + ": ")
        if tries.isdigit():
            tries = int(tries)
            
        if tries == secret:
            print("You Won")
        else:
            print("Please try again")
            count += 1
    print("It took you", count, "tries")
    
    
        
             
    
     
        