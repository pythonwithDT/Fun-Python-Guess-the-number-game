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
          