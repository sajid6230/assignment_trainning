""""
Write a Python program to guess a number between 1 and 9. Note : 
User is prompted to enter a guess. 
If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, 
user will get a "Well guessed!" message, and the program will exit
"""


import random



magic_number = random.randint(1,9)
while True:
    number = input("Guess a number between 1 to 9: ")
    num = int(number)
    if 1 <= num <= 9:
        if (num == magic_number):
            print("Well guessed!")
            break
        else:
            print("try again")
    else:
        print("Please! input valid number")


